""" Customizes the postgresql.psycopg2 dialect to work with Hawq. """

from sqlalchemy.dialects.postgresql import pg_catalog, aggregate_order_by, psycopg2
from sqlalchemy import schema, select, bindparam, sql
from sqlalchemy.types import TEXT
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Delete
from sqlalchemy.sql.schema import Table

from functools import lru_cache
from .ddl import HawqDDLCompiler


class HawqDialect(psycopg2.PGDialect_psycopg2):
    '''
    Main dialect class. Used by the engine to compile sql
    '''

    construct_arguments = [
        (
            schema.Table,
            {
                'partition_by': None,
                'inherits': None,
                'distributed_by': None,
                'bucketnum': None,
                'appendonly': None,
                'orientation': None,
                'compresstype': None,
                'compresslevel': None,
                'on_commit': None,
                'tablespace': None,
            },
        )
    ]
    ddl_compiler = HawqDDLCompiler
    name = 'hawq'
    supports_statement_cache = False

    def initialize(self, connection):
        """
        Override implicit_returning = True of postgresql dialect
        """
        super().initialize(connection)

        self.implicit_returning = False
        self.supports_native_uuid = False
        self.update_returning = False
        self.delete_returning = False
        self.insert_returning = False
        self.update_returning_multifrom = False
        self.delete_returning_multifrom = False

    @compiles(Delete, 'hawq')
    def visit_delete_statement(element, compiler, **kwargs):  # pylint: disable=no-self-argument
        """
        Allows a version of the delete statement to get compiled - the version
        that is effectively the same as truncate.

        Any filters on the delete statement result in an Exception.
        """
        delete_stmt_table = compiler.process(element.table, asfrom=True, **kwargs)
        filters_tuple = element.get_children()
        if not filters_tuple:
            return 'TRUNCATE TABLE {}'.format(delete_stmt_table)
        items = [item for item in element.get_children()]

        # check if filters_tuple contains only one item, and it's the table
        if (
            len(items) == 1
            and isinstance(items[0], Table)
            and compiler.process(items[0], asfrom=True, **kwargs) == delete_stmt_table
        ):
            return 'TRUNCATE TABLE {}'.format(delete_stmt_table)

        raise NotImplementedError('Delete statement with filter clauses not implemented for Hawq')

    def get_isolation_level_values(self, dbapi_conn):
        # note the generic dialect doesn't have AUTOCOMMIT, however
        # all postgresql dialects should include AUTOCOMMIT.
        # NB hawq doesn't support REPEATABLE READ
        return (
            "AUTOCOMMIT",
            "SERIALIZABLE",
            "READ UNCOMMITTED",
            "READ COMMITTED",
        )
    
    def _pg_class_filter_scope_schema(
        self, query, schema, scope, pg_class_table=None
    ):
        if pg_class_table is None:
            pg_class_table = pg_catalog.pg_class
        query = query.join(
            pg_catalog.pg_namespace,
            pg_catalog.pg_namespace.c.oid == pg_class_table.c.relnamespace,
        )

        # if scope is ObjectScope.DEFAULT:
        #     query = query.where(pg_class_table.c.relpersistence != "t")
        # elif scope is ObjectScope.TEMPORARY:
        #     query = query.where(pg_class_table.c.relpersistence == "t")

        if schema is None:
            query = query.where(
                pg_catalog.pg_table_is_visible(pg_class_table.c.oid),
                # ignore pg_catalog schema
                pg_catalog.pg_namespace.c.nspname != "pg_catalog",
            )
        else:
            query = query.where(pg_catalog.pg_namespace.c.nspname == schema)
        return query
    
    @lru_cache()
    def _enum_query(self, schema):
        # lbl_agg_sq = (
        #     select(
        #         pg_catalog.pg_enum.c.enumtypid,
        #         sql.func.array_agg(
        #             aggregate_order_by(
        #                 # NOTE: cast since some postgresql derivatives may
        #                 # not support array_agg on the name type
        #                 pg_catalog.pg_enum.c.enumlabel.cast(TEXT),
        #                 pg_catalog.pg_enum.c.enumsortorder,
        #             )
        #         ).label("labels"),
        #     )
        #     .group_by(pg_catalog.pg_enum.c.enumtypid)
        #     .subquery("lbl_agg")
        # )

        query = (
            select(
                pg_catalog.pg_type.c.typname.label("name"),
                pg_catalog.pg_type_is_visible(pg_catalog.pg_type.c.oid).label(
                    "visible"
                ),
                pg_catalog.pg_namespace.c.nspname.label("schema"),
                # lbl_agg_sq.c.labels.label("labels"),
                pg_catalog.pg_type.c.typname.label("labels"),
            )
            .join(
                pg_catalog.pg_namespace,
                pg_catalog.pg_namespace.c.oid
                == pg_catalog.pg_type.c.typnamespace,
            )
            # .outerjoin(
            #     lbl_agg_sq, pg_catalog.pg_type.c.oid == lbl_agg_sq.c.enumtypid
            # )
            .where(pg_catalog.pg_type.c.typtype == "e")
            .order_by(
                pg_catalog.pg_namespace.c.nspname, pg_catalog.pg_type.c.typname
            )
        )

        return self._pg_type_filter_schema(query, schema)
    

    @lru_cache()
    def _constraint_query(self, is_unique):
        con_sq = (
            select(
                pg_catalog.pg_constraint.c.conrelid,
                pg_catalog.pg_constraint.c.conname,
                0,
                sql.func.unnest(pg_catalog.pg_constraint.c.conkey).label(
                    "attnum"
                ),
                sql.func.generate_subscripts(
                    pg_catalog.pg_constraint.c.conkey, 1
                ).label("ord"),
                pg_catalog.pg_description.c.description,
            )
            .outerjoin(
                pg_catalog.pg_description,
                pg_catalog.pg_description.c.objoid
                == pg_catalog.pg_constraint.c.oid,
            )
            .where(
                pg_catalog.pg_constraint.c.contype == bindparam("contype"),
                pg_catalog.pg_constraint.c.conrelid.in_(bindparam("oids")),
            )
            .subquery("con")
        )

        attr_sq = (
            select(
                con_sq.c.conrelid,
                con_sq.c.conname,
                0,
                con_sq.c.description,
                con_sq.c.ord,
                pg_catalog.pg_attribute.c.attname,
            )
            .select_from(pg_catalog.pg_attribute)
            .join(
                con_sq,
                sql.and_(
                    pg_catalog.pg_attribute.c.attnum == con_sq.c.attnum,
                    pg_catalog.pg_attribute.c.attrelid == con_sq.c.conrelid,
                ),
            )
            .where(
                # NOTE: restate the condition here, since pg15 otherwise
                # seems to get confused on pscopg2 sometimes, doing
                # a sequential scan of pg_attribute.
                # The condition in the con_sq subquery is not actually needed
                # in pg15, but it may be needed in older versions. Keeping it
                # does not seems to have any inpact in any case.
                con_sq.c.conrelid.in_(bindparam("oids"))
            )
            .subquery("attr")
        )

        constraint_query = (
            select(
                attr_sq.c.conrelid,
                sql.func.array_agg(
                    # NOTE: cast since some postgresql derivatives may
                    # not support array_agg on the name type
                    aggregate_order_by(
                        attr_sq.c.attname.cast(TEXT), attr_sq.c.ord
                    )
                ).label("cols"),
                attr_sq.c.conname,
                sql.func.min(attr_sq.c.description).label("description"),
            )
            .group_by(attr_sq.c.conrelid, attr_sq.c.conname)
            .order_by(attr_sq.c.conrelid, attr_sq.c.conname)
        )

        if is_unique:
            # if self.server_version_info >= (15,):
            #     constraint_query = constraint_query.join(
            #         pg_catalog.pg_index,
            #         attr_sq.c.conindid == pg_catalog.pg_index.c.indexrelid,
            #     ).add_columns(
            #         sql.func.bool_and(
            #             pg_catalog.pg_index.c.indnullsnotdistinct
            #         ).label("indnullsnotdistinct")
            #     )
            # else:
            constraint_query = constraint_query.add_columns(
                sql.false().label("indnullsnotdistinct")
            )
        else:
            constraint_query = constraint_query.add_columns(
                sql.null().label("extra")
            )
        return constraint_query
#from manifest.base_manifest import AGBaseManifest


class AGQueryManifest:  #(AGBaseManifest):
    # Documentation
    ag_author: str = "Michael Lundager"
    ag_last_updated: str = "2022-08-10"
    ag_version: str = "0.8"
    ag_status: str = "in-development"  # pending, in-development, test, live, error
    ag_type: str = "utilities"  # model, controller, serializer, widget

    schema_name: str = None
    table_name: str = None
    id_name: str = None
    alias_name: str = None
    inner_join: list = None
    left_join: list = None
    select: list = None           # List of columns in main table
    column_function: list = None
    window: list = None
    total: list = None
    where_string: str = None
    where: list = None
    where_and: list = None
    order_by: list = None
    up_relations: list = None
    down_relations: list = None
    rollup: list = None
    cube: list = None
    limit: int = None
    offset: int = None
    page: int = None

    query_parameter_list: list = None  # List of parameters used for building up query form
    
    def __init__(
        self,
        schema_name: str = None,
        table_name: str = None,
        id_name: str = None,
        alias_name: str = None,
        inner_join: list = None,
        left_join: list = None,
        select: list = None,
        column_function: list = None,
        window: list = None,
        total: list = None,
        where_string: str = None,
        where: list = None,
        where_and: str = None,
        order_by: list = None,
        up_relations: list = None,
        down_relations: list = None,
        rollup: list = None,
        cube: list = None,
        limit: int = None,
        offset: int = None,
        page: int = None
    ):

        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if id_name is not None:
            self.id_name = id_name
        if alias_name is not None:
            self.alias_name = alias_name
        if inner_join is not None:
            self.inner_join = inner_join
        if left_join is not None:
            self.left_join = left_join
        if select is not None:
            self.select = select
        if column_function is not None:
            self.column_function = column_function
        if window is not None:
            self.window = window
        if total is not None:
            self.total = total
        if where_string is not None:
            self.where_string = where_string
        if where is not None:
            self.where = where
        if where_and is not None:
            self.where_and = where_and
        if order_by is not None:
            self.order_by = order_by
        if up_relations is not None:
            self.up_relations = up_relations
        if down_relations is not None:
            self.up_relations = up_relations
        if rollup is not None:
            self.rollup = rollup
        if cube is not None:
            self.cube = cube
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if page is not None:
            self.page = page

    class Meta:
        abstract = True


class AGQueryParameterManifest:  #(AGBaseManifest):
    # Documentation
    ag_author: str = "Michael Lundager"
    ag_last_updated: str = "2022-08-10"
    ag_version: str = "0.8"
    ag_status: str = "in-development"  # pending, in-development, test, live, error
    ag_type: str = "utilities"  # model, controller, serializer, widget

    name: str = None
    label: str = None
    widget_type: str = None
    url: str = None  # In user select
    description: str = None
    target: str = None  # {{ target }} string replacement place in query JSON

    def __init__(
        self,
        name: str = None,
        label: str = None,
        widget_type: str = None,
        url: str = None,
        description: str = None,
        target: str = None
    ):

        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if widget_type is not None:
            self.widget_type = widget_type
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description
        if target is not None:
            self.target = target

    class Meta:
        abstract = True


class AGReportManifest:  #(AGBaseManifest):
    # Documentation
    ag_author: str = "Michael Lundager"
    ag_last_updated: str = "2022-08-10"
    ag_version: str = "0.8"
    ag_status: str = "in-development"  # pending, in-development, test, live, error
    ag_type: str = "utilities"  # model, controller, serializer, widget

    icon: str = None
    name: str = None
    url: str = None
    description: str = None
    report_format: dict = None  # JSON that describes how to format the output of the report
    output_format: str = None   # excel, html, pdf
    query: AGQueryManifest = None

    def __init__(
        self,
        icon: str = None,
        name: str = None,
        url: str = None,
        description: str = None,
        report_format: dict = None,
        output_format: str = None,
        query: AGQueryManifest = None
    ):

        if icon is not None:
            self.icon = icon
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description
        if report_format is not None:
            self.report_format = report_format
        if output_format is not None:
            self.output_format = output_format
        if query is not None:
            self.query = query

    class Meta:
        abstract = True


class AGReportFormat:
    # Documentation
    ag_author: str = "Michael Lundager"
    ag_last_updated: str = "2022-08-10"
    ag_version: str = "0.8"
    ag_status: str = "in-development"  # pending, in-development, test, live, error
    ag_type: str = "utilities"  # model, controller, serializer, widget

    report_title: str = None
    page_title: str = None
    row: str = None
    page_footer: str = None
    group_list: list = None

    def __init__(
        self,
        report_title: str = None,
        page_title: str = None,
        row: str = None,
        page_footer: str = None,
        group_list: list = None
    ):
        if report_title is not None:
            self.report_title = report_title
        if page_title is not None:
            self.page_title = page_title
        if row is not None:
            self.row = row
        if page_footer is not None:
            self.page_footer = page_footer
        if group_list is not None:
            self.group_list = group_list

    class Meta:
        abstract = True


class AGReportGroup:
    title: str = None,
    row: str = None,
    footer: str = None

    def __init__(
        self,
        title: str = None,
        row: str = None,
        footer: str = None
    ):
        if title is not None:
            self.title = title
        if row is not None:
            self.row = row
        if footer is not None:
            self.footer = footer

    class Meta:
        abstract = True

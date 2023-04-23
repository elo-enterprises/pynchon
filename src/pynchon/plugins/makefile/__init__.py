# @common.kommand(
#     name="makefile",
#     parent=groups.gen,
#     formatters=dict(markdown=constants.T_FIXME),
#     options=[
#         options.format_markdown,
#         click.option(
#             "--output",
#             "-o",
#             default="docs/MAKE.md",
#             help=("output file to write.  (optional)"),
#         ),
#         options.stdout,
#         options.header,
#     ],
# )
# def gen_makefiles(output, format, stdout, header):
#     """
#     Generate documents for project makefiles
#     """

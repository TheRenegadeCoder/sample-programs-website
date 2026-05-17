import datetime

import subete


def get_program_datetimes(program: subete.SampleProgram) -> list[datetime.datetime | None]:
    """Get list of date/times for a sample program.

    :param subete.SampleProgram program: Sample program to get date/times for.
    :return: List of date/times for sample program
    """
    return [program.created(), program.modified(), program.doc_created(), program.doc_modified()]

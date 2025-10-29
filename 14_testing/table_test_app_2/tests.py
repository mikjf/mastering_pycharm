import pytest
import core


def test_there_are_tables_available():
    choice = 1
    one_tables = core.find_available(choice)
    assert len(one_tables)


def test_table_can_be_booked():
    table = core.all_tables()[0]
    booked_table = core.book_table(table.table_id)
    assert table.is_booked
    assert table.table_id == booked_table.table_id


def test_cannot_book_a_nonexistant_table():
    with pytest.raises(core.EntityNotFoundError):
        core.book_table('not-a-table-id')


def test_cannot_book_a_booked_table():
    table = core.find_available(2)[0]
    core.book_table(table.table_id)

    # add exception if table is booked
    with pytest.raises(core.TableUnavailableError):
        print("Pushing our luck!")
        core.book_table(table.table_id)

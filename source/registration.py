from aiogram.fsm.state import StatesGroup, State


class FSMFillForm(StatesGroup):
    fill_first_name = State()
    fill_second_name = State()


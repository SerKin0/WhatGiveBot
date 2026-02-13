from aiogram.fsm.state import State, StatesGroup


class FSMFillForm(StatesGroup):
    fill_first_name = State()
    fill_second_name = State()

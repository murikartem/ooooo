from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from loader import router

class Reg_form(StatesGroup):
    name = State()
    age = State()
    gender = State()

@router.message(Command('reg'))
async def start_reg(message: types.Message, state: FSMContext):
    await state.set_state(Reg_form.name)
    await message.answer('напиши свое имя')

@router.message(Reg_form.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg_form.age)
    await message.answer('а сейчас напиши свой возраст')

@router.message(Reg_form.age)
async def get_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Reg_form.gender)
    await message.answer('Теперь напиши свой пол')

@router.message(Reg_form.gender)
async def get_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    data = await state.get_data()
    name = data['name']
    age = data['age']
    gender = data['gender']
    await state.clear()
    await message.answer(('Регистрация завершена\n'
                          f'имя{name}\n'
                          f'возраст{age}\n'
                          f'пол{gender}\n'))

@router.message(Command('cancel'))
async def restart(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer('Регистрация отменена')

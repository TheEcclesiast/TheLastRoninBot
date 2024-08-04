from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message



router = Router()



@router.message(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Приветствую вас, {message.from_user.full_name} в нашем рекламном боте. \nЗдесь вы можете купить рекламу для вашего товара на маркетплейсе для лучших продаж\n Из важного хотим осведомить о продаже товаров категории 18+: Такие посты не публикуются и деньги за них не возвращаются. В остальном с Политикой приватности и Часто задаваемыми вопросами вы можете ознакомиться по их же командам. Приятного пользования!')

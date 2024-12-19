from fastapi import FastAPI, Path
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/", tags=["default"])
async def Get_Main_Page():
    return "Главная страница"

@app.get("/user/admin", tags=["default"])
async def Get_Admin_Page():
    return JSONResponse(content={"message": "Вы вошли как администратор"})

@app.get("/user/{user_id}", tags=["default"])
async def Get_User_Number(
    user_id: int = Path(
        ...,
        ge=1,  # минимальное значение
        le=100,  # максимальное значение
        description="ID пользователя (целое число от 1 до 100)",
        example=1  # пример значения
    )
):
    return JSONResponse(content={"message": f"Вы вошли как пользователь № {user_id}"})

@app.get("/user/{username}/{age}", tags=["default"])
async def Get_User_info(
    username: str = Path(
        ...,
        min_length=5,
        max_length=20,
        description="Имя пользователя (строка от 5 до 20 символов)",
        example="johndoe"  # пример значения
    ),
    age: int = Path(
        ...,
        ge=18,
        le=120,
        description="Возраст пользователя (целое число от 18 до 120)",
        example=25  # пример значения
    )
):
    return JSONResponse(content={"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"})


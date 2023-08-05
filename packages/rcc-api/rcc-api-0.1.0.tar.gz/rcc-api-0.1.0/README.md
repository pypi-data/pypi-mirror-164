# RustCheatCheck API
Удобная обертка для взаимодействия с апи [RCC](https://rustcheatcheck.ru/). 
# Как начать?

## Установка 
```
pip install rcc-api
```
## Взаимодействие
```python
import asyncio
import RCC


async def main():
    api = RCC.API("TOKEN/KEY")

    # Здесь показаны не все методы, более подробнее информация
    # Находится здесь https://rustcheatcheck.ru/panel/getapi
    # Некоторые поля/методы названы более правильно(по моему мнению)
    # Ваш редактор в любом случае вам подскажет

    # Получение информация об аккаутне
    player = await api.get_info(76561198021247080)
    print(player.steamid)  # 76561198021247080
    print(player.rcc_checks)  # 7
    checks = player.checks
    print(checks[1].time)  # 2019-01-08 16:53:13+00:00
    print(checks[1].server_name)  # MagicRust
    bans = player.bans
    print(bans[0].reason)  # мамкин_крашер
    print(bans[0].active)  # False
    print(bans[0].ban_date)  # 2019-06-11 12:01:07+00:00ет

    # Выдача доступа к чекеру
    response = await api.start_check(76561198021247080,  moder_steamid=76561198021247080)
    print(response.status)  # success
    print(response.error)  # None

    # Выдача бана
    response = await api.ban_player(76561198021247080, "macros")
    print(response.status)  # success
    print(response.error)  # None

    # Снятие бана
    response = await api.unban_player(76561198021247080)
    print(response.status)  # success
    print(response.error)  # None

    # Работа с ошибками
    try:
        player = await api.get_info(62485679287628672076)
    except RCC.exceptions.RCCErrors as e:
        print(e)


asyncio.run(main())

```

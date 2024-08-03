Репозиторий для написания кода в игре [Sceeps](https://screeps.com) на питоне

Для этого за основу был взят репозиторий [screeps-starter-python](https://github.com/daboross/screeps-starter-python), в котором в папках `/js_files`, `/src/defs` были описана интеграция с JS кодом самой игры

Далее предлагается в репозитории писать логику самого ИИ для игры (в папке `/src`)

----

1) Настройка работы с кодом (для Windows): 
нужные установки ПО (если ещё какие-то не установлены)

* Установка Visual Code 
* Установка Git 

ссылка для скачивания установщика: [https://git-scm.com/download/win](https://git-scm.com/download/win)

при установке можно оставлять все дефолтные значения, но сам путь установки я бы рекомендовал не делать дефолтный:
лучше сделать отдельную папку для всяких таких Установок (напр `C:\Tools\`), в которой создавать 


* Установка Python

ссылка для скачивания установщика: [https://www.python.org/downloads/](https://www.python.org/downloads/)

опять же - при установке можно оставлять всё дефолтное
но если тут устанавливать в какую-нибудь `C:\Tools\`, то там будет где-то пункт про "Добавить в PATH" нужно поставить, чтобы добавлялось

* Установка Node.js

ссылка для скачивания установщика: [https://nodejs.org/en/download/prebuilt-installer](https://nodejs.org/en/download/prebuilt-installer)

тут ВАЖНО выбирать установщик версии не выше версии `16.20.2` - я бы выбирал `v.15.14.0` на всякий
(с более высокими не работает сборка - на это есть issue в исъодном репозитории)

и тоже рекомендую установить в `Tools` (и там по-моему тоже что-то про PATH есть)

----------


2) Далее закачиваем сам этот репозиторий:

в консоли переходим в папку в которую хотим закачать весь код и вызываем
```
git clone https://github.com/ScreepsAiProgrammiring/screeps-pythonAI.git
```

после этого эту папку можно открыть в Visual Code - всё должно красиво подсвечиваться

----

3) Для загрузки кода в саму игру на сервере

Нужно, чтобы внутренний скрипт смог авторизоваться в системе, для этого:
 - копируем файл `config.default.json` в папке, называем его `config.json`
 - в этом файле нужно заполнить поле токен, он будет вида `"a1a11a11-1111-1111-a1aa-a111aa1a11a1"`
 - его можно получить в настройках пользователя в самой игре: [браузерная ссылка](https://screeps.com/a/#!/account/auth-tokens)
    Для этого нажимаем `Generate token` с выбранным тумблером `Full access`


После этого запускаем сам скрипт, который закидывает код на сервер:
из основной папки, в терминале вводим
```
py build.py
```

После этого в самой игре код должен обновиться

---

P.S. выше я попытался выжать информацию по установке описанную в документации из папки [books](book/README.md) - если интересно почитать, можно дойти ещё туда почитать
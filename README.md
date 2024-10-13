![logo](https://github.com/legitbox/Economy-Pilot/blob/main/EconomyPilotLogo.gif?raw=true)
# EconomyPilot<br>
This is a system/api plugin for an economy system for the endstone server software<br>

### Features<br>
- multithreaded SQLite database for fast and simple operations locally<br>
- External Mysql/MariaDB database support for more advanced users<br>
- the ability to use commands as an api to interact with other plugins<br>
- you can use custom symbols for currency<br>

### Installation<br>
Drag and drop the .whl file that you can get from releases and put it in your endstone's plugin folder<br>

### File Structure<br>
```
config/
├─ economy-pilot.toml
databases/
├─ economy-pilot/
│  ├─ database.db
```
<br>
- Configuration file `economy-pilot.toml`<br>
- Database file `database.db`<br>

### Command usage<br>
- Player commands<br><br>
`/balance or /bal` - if executed by the player it will give the players current balance
<br><br>
`/pay <username: str> <amount: int>` - if executed by the player it will let the player pay money to an another user, <br>for example `/pay legtibox7811 150`

- Server commands [needs op]<br>
`/serverpay <player: str> <amount: int>` - if executed by the server it will transfer money to the players balance, <br>for example `/serverpay legitbox7811 150`
<br><br>
`/serverdeduct <player: str> <amount: int>` - if executed by the server it will deduct money from the players balance, <br>for example `/serverdeduct legitbox7811 150`
<br><br>
`/serverbalance <player: str>` - if executed by the server it will show the selected player's balance, <br>for example `/serverlbalance legitbox7811`
<br><br>
`/setbalance <player: str> <balance: int>` - if executed by the server it will set the players balance to what you have selected, <br>for example `/setbalance legitbox7811 0`
<br><br>
`/deluser <player: str>` - if executed by the server it will remove the user's data from the database, <br>for example `/deluser legitbox7811`
<br><br>
`/nukedatabase` - WARNING!!! Nukes the database and stops the server

### How to use Economy Pilot in your own plugin!<br>
You can use the Economy API in your own python plugin by putting ![database_issuer](https://github.com/legitbox/Economy-Pilot/blob/main/for_devs/database_issuer.py) file inside your project and using its functions, you can directly run commands to interact with the Economy Pilot's database for better speed<br>

Note! - there are comments inside the python file that explain what each function does and what it needs to work
Note! - to make the database_issuer work you will need to add this dependancie in your project under the [project] tag
```toml
dependencies = [
  "PyMySQL"
]
```

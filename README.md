# discdb

discdb is a Python library for dealing with word pluralization.

## Installation

Using pip and git to install discdb.

```bash
pip install git+https://github.com/Hunter2807/discdb.git
```

## Usage
---
```python
import discdb

bot = commands.Bot(...)
bot.db = discdb.DiscDB(bot)

@bot.command()
async def test(ctx):
    msg = await bot.db.get_json(...)
    some_dict = {
        "1": "One",
        "2": "Two"
    }
    await bot.db.save_json(some_dict)

```
---
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

---
## License
[MIT](https://choosealicense.com/licenses/mit/)
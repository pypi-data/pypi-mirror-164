# DNA CRYPT

DNA CRYPTO is a package to use in python that uses DNA code-based encryption to hide messages.

## Getting Started

Just use pip to install it! 

### Prerequisites

To use dnacrypt is necessary have installed random package and unidecode package.

```
pip install random
pip install unidecode
```

### Installing

Check that the packages random and unidecode have been installed

Use this command in terminal to verify it:

```
pip freeze
```

*If necessery install packages random and unidecode!

And install DNA CRYPT using this command in terminal:

```
pip install dnacrypt
```

If you want, install dnacrypt and use command status() to verify status of package.

## Running the test


dnacrypt uses third-party packages to run.


### Test status dnacrypt

```
import dnacrypt
print(dnacrypt.dnacrypt.required)
print(dnacrypt.dnacrypt.status())
```

### See how to use it

```
import dnacrypt 
print(dnacrypt.dnacrypt.use)
```

### See description

```
import dnacrypt
print(dnacrypt.dnacrypt.description)
```


### How to use it

## To encrypt the message use this command:

```
dnacrypt.dnacrypt('encrypt','Esse script foi feito pensando melhorar minhas skills')
```

## Output

UUUUUCUUAUUGUCUUCCUCAUCGUAUUACGCAUGUUGCGCGUGGCUUCUCCUACUGCCUCCCCCACCGCAUCACCAACAGCGUCGCCGAAUGUCUAGAAGACGGGAUAGACGCAGCACUAAGAGGGAUAUUAAAACUGAUAUUCGGACUAGGAAAGAUAAGCGGAACAGACAGAACCGAAAAGAUAAUCGGACGAUAAAAAGCCAGAGCGAUAAUACUAACAUACAGAGAGAUAGAACAACUACGACGAGAUAAUUUUUCUUAUUGUCUUCCUCAUCGUAUUACGCAUGUUGCGCGUGGCUUCUCCUACUGCCUCCCCCACCGCAU

## To decrypt the message use this command:

```
dnacrypt.dnacrypt('decrypt','UUUUUCUUAUUGUCUUCCUCAUCGUAUUACGCAUGUUGCGCGUGGCUUCUCCUACUGCCUCCCCCACCGCAUCACCAACAGCGUCGCCGAAUGUCUAGAAGACGGGAUAGACGCAGCACUAAGAGGGAUAUUAAAACUGAUAUUCGGACUAGGAAAGAUAAGCGGAACAGACAGAACCGAAAAGAUAAUCGGACGAUAAAAAGCCAGAGCGAUAAUACUAACAUACAGAGAGAUAGAACAACUACGACGAGAUAAUUUUUCUUAUUGUCUUCCUCAUCGUAUUACGCAUGUUGCGCGUGGCUUCUCCUACUGCCUCCCCCACCGCAU')
```

## Output

Esse script foi feito pensando melhorar minhas skills.

## Built With

* [VisualCode](Esse script foi feito pensando melhorar minhas skills) - The web framework used
* [CataLux](https://catalux.com.br/) - CataLux Labs


## Authors

* **Rodrigo Forti** - *Initial work* - [CataLux Python Labs](https://github.com/CataLux)

See also the list of [contributors](https://github.com/catalux/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This code was created to improve learning skills.
* Enjoy your self!

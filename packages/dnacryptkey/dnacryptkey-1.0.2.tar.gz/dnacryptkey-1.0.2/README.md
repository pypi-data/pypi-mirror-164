# DNACRYPT-KEY

DNACRYPTO-KEY is a package to use in python that uses DNA code-based encryption to hide messages.

## Getting Started

Just use pip to install it! 

### Prerequisites

To use dnacrypt-key is necessary have installed random package and unidecode package.

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
pip install dnacrypt-key
```

If you want, install dnacrypt-key and use command status() to verify status of package.

## Running the test


dnacrypt uses third-party packages to run.


### Test status dnacrypt-key

```
import dnacrypt-key
print(dnacrypt-key.dnacrypt-key.required)
print(dnacrypt-key.dnacrypt-key.status())
```

### See how to use it

```
import dnacrypt-key 
print(dnacrypt-key.dnacrypt-key.use)
```

### See description

```
import dnacrypt-key
print(dnacrypt-key.dnacrypt-key.description)
```


### How to use it

## To encrypt the message use this command:

```
dnacrypt-key.dnacrypt-key('encrypt','Esse script foi feito pensando melhorar minhas skills','chavesecreta')
```

## Output

UUUUUCUUAUUGUCUUCCUCAUCGUAUUACGCAUGUUGCGCGUGGCUUCUCCUACUGCCUCCCCCACCGCAUCACCAACAGCGUCGCCGAAUGUCUAGAAGACGGGAUAGACGCAGCACUAAGAGGGAUAUUAAAACUGAUAUUCGGACUAGGAAAGAUAAGCGGAACAGACAGAACCGAAAAGAUAAUCGGACGAUAAAAAGCCAGAGCGAUAAUACUAACAUACAGAGAGAUAGAACAACUACGACGAGAUAAUUUUUCUUAUUGUCUUCCUCAUCGUAUUACGCAUGUUGCGCGUGGCUUCUCCUACUGCCUCCCCCACCGCAU

## To decrypt the message use this command:

```
dnacrypt-key.dnacrypt-key('decrypt','UUUUUCUUAUUGUCUUCCUCAUCGUAUUACGCAUGUUGCGCGUGGCUUCUCCUACUGCCUCCCCCACCGCAUCACCAACAGCGUCGCCGAAUGUCUAGAAGACGGGAUAGACGCAGCACUAAGAGGGAUAUUAAAACUGAUAUUCGGACUAGGAAAGAUAAGCGGAACAGACAGAACCGAAAAGAUAAUCGGACGAUAAAAAGCCAGAGCGAUAAUACUAACAUACAGAGAGAUAGAACAACUACGACGAGAUAAUUUUUCUUAUUGUCUUCCUCAUCGUAUUACGCAUGUUGCGCGUGGCUUCUCCUACUGCCUCCCCCACCGCAU','chavesecreta')
```

## Output

Esse script foi feito pensando melhorar minhas skills.

## Built With

* [VisualCode](Esse script foi feito pensando melhorar minhas skills) - The web framework used
* [CataLux](https://catalux.com.br/) - CataLux Labs


## Authors

* **Rodrigo Forti** - *Initial work* - [CataLux Python Labs](https://github.com/FortiHub)

See also the list of [contributors](https://github.com/catalux/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This code was created to improve learning skills.
* Enjoy your self!

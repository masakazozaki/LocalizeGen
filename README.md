LocalizeGen
====

auto-generate-localizeString from google spread sheet to iOS and Android Projects


## Description
simple automation scripts to create localizableString files to iOS and Android.

## Requirement
- Python3
  - No third party libraries required.
- **URL SHARED** Google Spread Sheet's Id
  
## Usage
```
$ python3 LocalizeGen.py {ios or android} {Spread Sheet Id} {Output Path(relative path)}
```
Just running script with 3 argument (platformName(`ios` or `android`), Spread Sheet Id, Output Path)

### example
```
$ python3 LocalizeGen.py ios 1A_i8k20E9lMLhziQ0ZrD4k_UcSbCKgKeKJIdPEeM5XQ /
```
## Google Spread Sheet Settings
- [sample](https://docs.google.com/spreadsheets/d/1A_i8k20E9lMLhziQ0ZrD4k_UcSbCKgKeKJIdPEeM5XQ/edit#gid=0)
- sheet ID Location in Sheet URL
  - `https://docs.google.com/spreadsheets/d/`**1A_i8k20E9lMLhziQ0ZrD4k_UcSbCKgKeKJIdPEeM5XQ**`/edit#gid=0` 

## Contribution
Contribution 

1. Fork it
2. Create your feature branch (git checkout -b hogehoge)
3. Commit your changes (git commit -m 'Add some feature')
4. Push to the branch (git push origin hogehoge)
5. Create new Pull Request

## Licence

[MIT LICENSE](https://github.com/MasakazOzaki/LocalizeGen/blob/master/LICENSE)

## Author

[Masakaz Ozaki](https://github.com/MasakazOzaki) masakaz@ieee.org

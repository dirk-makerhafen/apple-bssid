
## BSSID to Geolocation

This Python script queries the public Apple iPhone geolocation API to retrieve the geolocation of a given BSSID.

### Usage
```
./main.py 3a:80:88:ef:62:89
```

## Example Output: 
```
wifi {
  bssid: "4c:12:d4:2d:ef:27"
  location {
    latitude: 5156302642
    longitude: 912588138
    valeur_inconnue3: 28
    valeur_inconnue4: 3
    valeur_inconnue5: 21
    valeur_inconnue6: 12
    valeur_inconnue11: 62
    valeur_inconnue12: 235
  }
}
wifi {
  bssid: "4d:23:65:1:f2:95"
  location {
    latitude: 5156290054
    longitude: 192612743
    valeur_inconnue3: 27
    valeur_inconnue4: 3
    valeur_inconnue5: 22
    valeur_inconnue6: 23
    valeur_inconnue11: 62
    valeur_inconnue12: 138
  }
}
```

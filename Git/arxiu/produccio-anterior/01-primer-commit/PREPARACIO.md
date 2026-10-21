# Preparació per seguir la primera lliçó

El vídeo comença amb un repositori buit que ja s’ha creat i clonat. Aquesta
preparació és prèvia a les edicions i als commits de la demostració.

1. Comprova que tens Git i Python disponibles amb `git --version` i
   `python3 --version`. Al vídeo es fa servir una terminal amb `python3`.
2. Crea al teu compte de GitHub un repositori de pràctiques buit, per exemple
   `HelloGit`, sense afegir README, llicència o `.gitignore` inicials.
3. Copia’n l’URL i clona’l. Substitueix el marcador per l’adreça pròpia;
   no escriguis literalment els signes `<` i `>`:

   ```bash
   git clone <URL-del-repositori> HelloGit
   cd HelloGit
   ```

4. Configura la identitat d’autoria d’aquest repositori si encara no la tens:

   ```bash
   git config user.name "El teu nom"
   git config user.email "El teu correu"
   ```

   Aquestes ordres sense `--global` només afecten aquest repositori. La
   identitat dels commits i les credencials d’accés a GitHub són configuracions
   diferents. Cal tenir configurat l’accés per poder fer el push del vídeo.

5. Comprova els noms que farà servir l’exemple:

   ```bash
   git symbolic-ref --short HEAD
   git remote -v
   ```

   El vídeo utilitza `main` com a branca i `origin` com a remot. Si la branca
   buida té un altre nom, pots posar-li `main` amb `git branch -M main`.
   `origin` ha d’apuntar al teu repositori, no a una URL de mostra.

En aquest punt no hi ha commits ni el fitxer `helloGit.py`. Durant el vídeo
el crearàs amb aquest contingut:

```python
print("Hello Git!")
```

El segon canvi del vídeo el deixa així:

```python
print("Hola, Anna!")
```

Si ja tens una carpeta anomenada HelloGit, fes servir una carpeta nova de
pràctiques. Les comandes de clonació creen una còpia nova; no es tornen a
executar dins d’un projecte que ja tens clonat.

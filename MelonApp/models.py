# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from ckeditor.fields import RichTextField

#komandu makemigrations izvrsavas sve regularno
#komandu migrate izvrsavas python manage.py migrate --database=secondary (ili --database=default za primarnu bazu)
class Clan(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    ime = models.TextField(db_column='Ime', blank=True, null=True)
    prezime = models.TextField(db_column='Prezime', blank=True, null=True)
    pol = models.IntegerField(db_column='Pol', blank=True, null=True)
    grad = models.TextField(db_column='Grad', blank=True, null=True)
    klub = models.TextField(db_column='Klub', blank=True, null=True)
    datumrodjenja = models.IntegerField(db_column='DatumRodjenja', blank=True, null=True)
    brojtelefona = models.TextField(db_column='BrojTelefona', blank=True, null=True)
    email = models.TextField(db_column='Email', blank=True, null=True)
    jmbg = models.TextField(db_column='JMBG', blank=True, null=True)
    nacionalnost = models.TextField(db_column='Nacionalnost', blank=True, null=True)
    lozinka = models.TextField(db_column='Lozinka', blank=True, null=True)
    clanarina = models.TextField(db_column='Clanarina')
    validated = models.TextField(blank=True, null=True)
    odobrenje = models.TextField(blank=True, null=True)
    adresa = models.TextField(db_column='Adresa')
    lekarsko = models.TextField(db_column='Lekarsko')
    dana = models.TextField(db_column='dana',blank=True, null=True)
    dominantnaruka = models.IntegerField(db_column='DominantnaRuka', blank=True, null=True)
    omiljenapodloga = models.TextField(db_column='OmiljenaPodloga', blank=True, null=True)
    beleska = models.TextField(db_column='Beleska', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Clan'

class Kategorija(models.Model):
    clan = models.ForeignKey(Clan, models.DO_NOTHING, db_column='Clan_ID')
    sezona = models.IntegerField(db_column='Sezona')
    kategorija = models.TextField(db_column='Kategorija', blank=True, null=True)
    kategorija2 = models.TextField(db_column='Kategorija2', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kategorija'
        unique_together = (('clan', 'sezona'),)  # Composite key

class Rezultat(models.Model):
    clan = models.ForeignKey(Clan, models.DO_NOTHING, db_column='Clan_ID')
    tip = models.TextField(db_column='Tip')
    kategorija = models.TextField(db_column='Kategorija')
    sezona = models.IntegerField(db_column='Sezona')
    osvojenobodova = models.IntegerField(db_column='OsvojenoBodova', blank=True, null=True)
    mesto = models.IntegerField(db_column='Mesto')

    class Meta:
        managed = False
        db_table = 'Rezultat'
        unique_together = (('clan', 'tip', 'kategorija', 'sezona'),)  # Composite key



class Turnir(models.Model):
    turnir_id = models.AutoField(db_column='Turnir_ID', primary_key=True)  # Field name made lowercase.
    naziv = models.TextField(db_column='Naziv')  # Field name made lowercase.
    kategorija = models.TextField(db_column='Kategorija')  # Field name made lowercase.
    sezona = models.IntegerField(db_column='Sezona')  # Field name made lowercase.
    lozinka = models.TextField(db_column='Lozinka', blank=True, null=True)  # Field name made lowercase.
    prijavljivanje = models.IntegerField(db_column='Prijavljivanje')  # Field name made lowercase.
    pregled = models.TextField(db_column='Pregled')  # Field name made lowercase.
    sudija = models.TextField(db_column='Sudija', blank=True, null=True)  # Field name made lowercase.
    domacin = models.TextField(db_column='Domacin', blank=True, null=True)  # Field name made lowercase.
    itf = models.IntegerField(db_column='ITF')  # Field name made lowercase.
    masters = models.IntegerField(db_column='Masters')  # Field name made lowercase.
    bodoviaktivni = models.IntegerField(db_column='BodoviAktivni')  # Field name made lowercase.
    automatski = models.IntegerField(db_column='Automatski')  # Field name made lowercase.
    klub = models.TextField(db_column='Klub', blank=True, null=True)  # Field name made lowercase.
    lokacija = models.TextField(db_column='Lokacija', blank=True, null=True)  # Field name made lowercase.
    kontakt = models.TextField(db_column='Kontakt', blank=True, null=True)  # Field name made lowercase.
    satnica1 = models.TextField(db_column='Satnica')  # Field name made lowercase.
    sifra = models.TextField(db_column='Sifra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Turnir'


class Utakmica(models.Model):
    utakmica_id = models.AutoField(db_column='Utakmica_ID', primary_key=True)  # Field name made lowercase.
    nesto = models.IntegerField(db_column='Nesto')  # Field name made lowercase.
    turnir = models.ForeignKey(Turnir, models.DO_NOTHING, db_column='Turnir_ID')  # Field name made lowercase.
    kolo = models.IntegerField(db_column='Kolo')  # Field name made lowercase.
    bodovapobednik = models.IntegerField(db_column='BodovaPobednik')  # Field name made lowercase.
    bodovagubitnik = models.IntegerField(db_column='BodovaGubitnik')  # Field name made lowercase.
    tip = models.TextField(db_column='Tip')  # Field name made lowercase.
    kategorija = models.TextField(db_column='Kategorija')  # Field name made lowercase.
    pol = models.TextField(db_column='Pol')  # Field name made lowercase.
    rezultat = models.TextField(db_column='Rezultat', blank=True, null=True)  # Field name made lowercase.
    sistem = models.TextField(db_column='Sistem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Utakmica'

class ClanTurnir(models.Model):
    clan = models.ForeignKey(Clan, models.DO_NOTHING, db_column='Clan_ID')
    turnir = models.ForeignKey(Turnir, models.DO_NOTHING, db_column='Turnir_ID')
    tip = models.TextField(db_column='Tip')
    kategorija = models.TextField(db_column='Kategorija', blank=True, null=True)
    osvojenobodova = models.IntegerField(db_column='OsvojenoBodova', blank=True, null=True)
    nosilac = models.IntegerField(db_column='Nosilac')

    class Meta:
        managed = False
        db_table = 'Clan__Turnir'
        unique_together = (('clan', 'turnir', 'tip'),)  # Composite key



class ClanUtakmica(models.Model):
    clan = models.ForeignKey(Clan, models.DO_NOTHING, db_column='Clan_ID')
    utakmica = models.ForeignKey(Utakmica, models.DO_NOTHING, db_column='Utakmica_ID')
    tim = models.IntegerField(db_column='Tim')
    pobednik = models.IntegerField(db_column='Pobednik')
    osvojenobodova = models.IntegerField(db_column='OsvojenoBodova')

    class Meta:
        managed = False
        db_table = 'Clan__Utakmica'
        unique_together = (('clan', 'utakmica'),)  # Composite key

class Satnica(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    clan = models.ForeignKey(Clan, models.DO_NOTHING, db_column='Clan_ID', blank=True, null=True)
    pol = models.TextField(db_column='Pol', blank=True, null=True)
    ime = models.TextField(db_column='Ime', blank=True, null=True)
    prezime = models.TextField(db_column='Prezime', blank=True, null=True)
    tip = models.TextField(db_column='Tip', blank=True, null=True)
    kategorija = models.TextField(db_column='Kategorija', blank=True, null=True)
    dan = models.TextField(db_column='Dan', blank=True, null=True)
    sat = models.TextField(db_column='Sat', blank=True, null=True)
    minut = models.TextField(db_column='Minut', blank=True, null=True)
    turnir = models.ForeignKey(Turnir, models.DO_NOTHING, db_column='Turnir_ID')

    class Meta:
        managed = False
        db_table = 'Satnica'


class Vesti(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')  # Auto-incrementing primary key
    text = models.TextField(db_column='Text',null=True)  # Field to store the text
    naslov = models.TextField(db_column='Naslov',null=True)
    potpis = models.TextField(db_column='Potpis', null=True)
    godina = models.IntegerField(db_column='Godina',null=True)  # Field to store the year
    date = models.DateField(db_column='Datum',null=True)  # Field to store the date

    class Meta:
        managed = True  # Django will manage the table
        db_table = 'Vesti'  # Explicit table name

class FAQ(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')  # Auto-incrementing primary key
    pitanje = models.TextField(db_column='Pitanje',null=True)  # Field to store the text
    odgovor = models.TextField(db_column='Odgovor', null=True)  # Field to store the text
    redosled = models.IntegerField(db_column='Redosled',null=True)

    class Meta:
        managed = True  # Django will manage the table
        db_table = 'Pitanja'  # Explicit table name

class Galerija(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')  # Auto-incrementing primary key
    opis = models.TextField(db_column='Opis',null=True)  # Field to store the text
    src = models.TextField(db_column='Src', null=True)  # Field to store the text
    godina = models.IntegerField(db_column='Godina', null=True)  # Field to store the year
    date = models.DateField(db_column='Datum', null=True)  # Field to store the date

    class Meta:
        managed = True  # Django will manage the table
        db_table = 'Galerija'  # Explicit table name

class Sadrzaj(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')  # Auto-incrementing primary key
    putanja = models.TextField(db_column='Path', null=True)
    #tekst = models.TextField(db_column='Tekst')  # Field to store the text
    tekst=RichTextField(db_column='Tekst',null=True)
    poslednjeazurirano = models.DateField(db_column='PoslednjeAzurirano', null=True)  # Field to store the date

    class Meta:
        managed = True  # Django will manage the table
        db_table = 'Sadrzaj'  # Explicit table name
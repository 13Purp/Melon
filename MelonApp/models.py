# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# komandu makemigrations izvrsavas sve regularno
# komandu migrate izvrsavas python manage.py migrate --database=secondary (ili --database=default za primarnu bazu)
class Firma(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    naziv = models.CharField(db_column='NAZIV',max_length=30)  # Field name made lowercase.
    sprat = models.IntegerField(db_column='SPRAT', blank=True, null=True)  # Field name made lowercase.
    strana_sveta = models.CharField(db_column='STRANA_SVETA', blank=True, null=True,max_length=30)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', blank=True, null=True,max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', blank=True, null=True,max_length=30)  # Field name made lowercase.
    tip = models.CharField(db_column='TIP', blank=True, null=True,max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FIRMA'


class Kartice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    encrypted_card = models.BinaryField(db_column='ENCRYPTED_CARD', blank=True, null=True)  # Field name made lowercase.
    idk = models.ForeignKey('Korisnik', models.DO_NOTHING, db_column='IDK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KARTICE'


class Korisnik(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    ime = models.CharField(db_column='IME',max_length=30)  # Field name made lowercase.
    prezime = models.CharField(db_column='PREZIME',max_length=30)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', blank=True, null=True,max_length=30)  # Field name made lowercase.
    broj_telefona = models.CharField(db_column='BROJ_TELEFONA', blank=True, null=True,max_length=30)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', blank=True, null=True,max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', blank=True, null=True,max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KORISNIK'


class Popust(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    idk = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='IDK',max_length=30)  # Field name made lowercase.
    encrypted_card = models.BinaryField(db_column='ENCRYPTED_CARD', blank=True, null=True,max_length=30)  # Field name made lowercase.
    iskoriscen = models.BooleanField(db_column='ISKORISCEN', blank=True, null=True,max_length=30)  # Field name made lowercase.
    idp = models.ForeignKey('Promocija', models.DO_NOTHING, db_column='IDP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POPUST'


class PopustFirma(models.Model):
    idp = models.OneToOneField('Promocija', models.DO_NOTHING, db_column='IDP',
                               primary_key=True)  # Field name made lowercase. The composite primary key (IDP, IDF) found, that is not supported. The first column is selected.
    idf = models.ForeignKey(Firma, models.DO_NOTHING, db_column='IDF')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POPUST_FIRMA'


class Pos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    idf = models.ForeignKey(Firma, models.DO_NOTHING, db_column='IDF')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POS'


class Promocija(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    idf = models.ForeignKey(Firma, models.DO_NOTHING, db_column='IDF')  # Field name made lowercase.
    iskorisceno = models.IntegerField(db_column='ISKORISCENO', blank=True, null=True)  # Field name made lowercase.
    ukupno = models.IntegerField(db_column='UKUPNO', blank=True, null=True)  # Field name made lowercase.
    minimalan_iznos = models.IntegerField(db_column='MINIMALAN_IZNOS', blank=True,
                                          null=True)  # Field name made lowercase.
    od = models.DateTimeField(db_column='OD', blank=True, null=True)  # Field name made lowercase.
    do = models.DateTimeField(db_column='DO', blank=True, null=True)  # Field name made lowercase.
    flat_popust = models.IntegerField(db_column='FLAT_POPUST', blank=True, null=True)  # Field name made lowercase.
    procenat_popust = models.IntegerField(db_column='PROCENAT_POPUST', blank=True,
                                          null=True)  # Field name made lowercase.
    max_iznos = models.IntegerField(db_column='MAX_IZNOS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROMOCIJA'


class Transakcije(models.Model):
    id_t = models.AutoField(db_column='ID_T', primary_key=True, blank=True)  # Field name made lowercase.
    id_f = models.ForeignKey(Firma, models.DO_NOTHING, db_column='ID_F')  # Field name made lowercase.
    encrypted_card = models.BinaryField(db_column='ENCRYPTED_CARD', blank=True, null=True)  # Field name made lowercase.
    iznos = models.IntegerField(db_column='IZNOS', blank=True, null=True)  # Field name made lowercase.
    datum_vreme = models.DateTimeField(db_column='DATUM_VREME', blank=True, null=True)  # Field name made lowercase.
    popust = models.BooleanField(db_column='POPUST', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRANSAKCIJE'


class Parking(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True)  # Auto-increment primary key
    encrypted_card = models.BinaryField(db_column='ENCRYPTED_CARD', blank=True, null=True)  # Field for encrypted card
    iznos = models.IntegerField(db_column='IZNOS', blank=True, null=True)  # Field for amount

    class Meta:
        managed = False  # Don't let Django manage the database schema
        db_table = 'PARKING'  # Table name in the database

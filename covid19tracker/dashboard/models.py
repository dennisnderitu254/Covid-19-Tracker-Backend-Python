from django.db import models


class Covid19Data(models.Model):
    dataid = models.AutoField(db_column='DataID', primary_key=True)  # Field name made lowercase.
    countryid = models.ForeignKey('Country', models.DO_NOTHING, db_column='CountryID')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    confirmedcases = models.IntegerField(db_column='ConfirmedCases')  # Field name made lowercase.
    recoveredcases = models.IntegerField(db_column='RecoveredCases')  # Field name made lowercase.
    fatalities = models.IntegerField(db_column='Fatalities')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COVID19Data'


class Country(models.Model):
    countryid = models.AutoField(db_column='CountryID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    isocode = models.CharField(db_column='ISOCode', max_length=50)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.
    subregion = models.CharField(db_column='Subregion', max_length=50)  # Field name made lowercase.
    regionid = models.ForeignKey('Region', models.DO_NOTHING, db_column='RegionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Country'


class Region(models.Model):
    regionid = models.AutoField(db_column='RegionID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Region'

class Cases(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    state = models.CharField(db_column='State', max_length=45)
    county = models.CharField(db_column='County', max_length=45)
    confirmed = models.CharField(db_column='Confirmed', max_length=45)
    deaths = models.CharField(db_column='Deaths', max_length=45)
    recovered = models.CharField(db_column='Recovered', max_length=45)

    class Meta:
        managed = False
        db_table = 'Cases'

from django.db import models

class Akun(models.Model):
	username = models.CharField(
		max_length=20,
		primary_key=True,
		)
	password = models.CharField(
		min_length=8,
		max_length=16,
		)
	tipe_akun = models.CharField(
		choice = (
			('ceo' : 'CEO'),
			('member' : 'Member'),
			)
		)
	nama = models.CharField(
		max_length=30,
		)
	alamat = models.CharField(
		max_length=50,
		)


class Kabid(models.Model):
	akun = models.OneToOneField(
		Akun,
		primary_key=True,
		)

class Anggota(models.Model):
	akun = models.OneToOneField(
		Akun,
		primary_key=True,
		)
	posisi = models.CharField(
		choice=(
			('pj' : 'Penanggung Jawab'),
			('ag' : 'Anggota'),
		)
	)



class Proyek(models.Model):
	kabid = models.ForeignKey(
		Kabid,
		)
	
class Proyek_PJ(models.Model):
	proyek = models.ForeignKey(
		Proyek,
		)
	penanggungjawab = models.ForeignKey(
		Anggota,
		)


class Proyek_AG(models.Model):
	proyek_pj = models.ForeignKey(
		Proyek_PJ,
		)
	anggota = models.ForeignKey(
		Anggota,
		)

class Resource(models.Model):
	

class Resource_Record(models.Model):
	proyek = models.ForeignKey(
		Proyek,
		)

 
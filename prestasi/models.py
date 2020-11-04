# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Prestasi(models.Model):
    index = models.BigIntegerField(blank=True, null=False, primary_key=True)
    timestamp = models.TextField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.
    email_address = models.TextField(db_column='Email Address', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_kompetisi = models.TextField(db_column='Nama Kompetisi', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nim = models.FloatField(db_column='NIM', blank=True, null=True)  # Field name made lowercase.
    nama = models.TextField(db_column='Nama', blank=True, null=True)  # Field name made lowercase.
    no_hp = models.FloatField(db_column='No. HP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lookup = models.TextField(db_column='LOOKUP', blank=True, null=True)  # Field name made lowercase.
    prestasi = models.TextField(db_column='Prestasi', blank=True, null=True)  # Field name made lowercase.
    keterangan = models.TextField(db_column='Keterangan', blank=True, null=True)  # Field name made lowercase.
    evidence_foto_sertifikat_surat_undangan_surat_tugas_field = models.TextField(db_column='Evidence (Foto, Sertifikat, Surat Undangan/Surat Tugas)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    evaluasi = models.TextField(db_column='Evaluasi', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.TextField(db_column='Updated By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status_follow_up = models.TextField(db_column='Status Follow Up', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ukm = models.TextField(db_column='UKM', blank=True, null=True)  # Field name made lowercase.
    bidang_ukm = models.TextField(db_column='Bidang UKM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bidang_prestasi = models.TextField(db_column='Bidang Prestasi', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tahun = models.FloatField(db_column='Tahun', blank=True, null=True)  # Field name made lowercase.
    triwulan = models.TextField(db_column='Triwulan', blank=True, null=True)  # Field name made lowercase.
    tw = models.TextField(db_column='TW', blank=True, null=True)  # Field name made lowercase.
    tahun_akademik = models.TextField(db_column='Tahun Akademik', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nim_nama = models.TextField(db_column='NIM & Nama', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fakultas = models.TextField(db_column='Fakultas', blank=True, null=True)  # Field name made lowercase.
    program_studi = models.TextField(db_column='Program Studi', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    angkatan = models.FloatField(db_column='Angkatan', blank=True, null=True)  # Field name made lowercase.
    short_fakultas = models.TextField(db_column='Short Fakultas', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tingkat = models.TextField(db_column='Tingkat', blank=True, null=True)  # Field name made lowercase.
    kategori_peserta = models.TextField(db_column='Kategori Peserta', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jumlah_pt = models.FloatField(db_column='Jumlah PT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kategori_jumlah_pt = models.TextField(db_column='Kategori Jumlah PT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    juara = models.TextField(db_column='Juara', blank=True, null=True)  # Field name made lowercase.
    penyelenggara = models.TextField(db_column='Penyelenggara', blank=True, null=True)  # Field name made lowercase.
    tanggal_pelaksanaan = models.TextField(db_column='Tanggal Pelaksanaan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kategori_juara = models.TextField(db_column='Kategori Juara', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sudah_menerima_beasiswa = models.FloatField(db_column='Sudah Menerima Beasiswa', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    proper_name = models.TextField(db_column='Proper Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    evidence_sudah_lengkap = models.TextField(db_column='Evidence Sudah Lengkap', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    evidence_belum_lengkap = models.TextField(db_column='Evidence Belum Lengkap', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_tidak_sesuai = models.TextField(db_column='Data Tidak Sesuai', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    penerima_beasiswa_2019 = models.FloatField(db_column='Penerima Beasiswa 2019', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    url_penyelenggara = models.TextField(db_column='URL Penyelenggara', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skor = models.FloatField(db_column='Skor', blank=True, null=True)  # Field name made lowercase.
    format_nama_file = models.TextField(db_column='Format Nama File', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'prestasi'

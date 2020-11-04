from rest_framework import serializers
from .models import Prestasi

class PrestasiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestasi
        fields = [
            'index',
            'email_address',
            'nama_kompetisi',
            'nim',
            'nama',
            'no_hp',
            'keterangan',
            'ukm',
            'tahun',
            'triwulan',
            'tahun_akademik',
            'fakultas',
            'program_studi',
            'angkatan',
            'url_penyelenggara',
            'juara'
        ]
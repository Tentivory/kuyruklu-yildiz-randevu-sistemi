#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kuyruklu Yildiz Randevu Sistemi — resmi protokol istemcisi."""

import random
import hashlib
from datetime import datetime, timedelta

KUYRUKLULAR = [
    "1P/Halley",
    "C/1995 O1 Hale-Bopp",
    "C/2020 F3 NEOWISE",
    "2P/Encke",
    "67P/Çuryumov-Gerasimenko",
    "C/2011 L4 PanSTARRS",
    "isimsiz utangac kuyruklu yildiz (katalog disi)",
]

SEBEPLER = [
    "sadece selam vermek",
    "kuyruk orneklemek",
    "yorgunluk izni sormak",
    "gunes etrafinda tur atma takvimi",
    "buz ornegi imzalatmak",
    "evrenin en uzun kahve molasini planlamak",
]


def protokol_no(ad: str) -> str:
    ham = f"{ad}-{datetime.utcnow().isoformat()}".encode()
    return "KYRS-" + hashlib.sha1(ham).hexdigest()[:10].upper()


def bekleme_suresi() -> str:
    yil = random.choice([3, 6, 12, 19, 36, 76, 133])
    gun = random.randint(1, 360)
    return f"{yil} yil {gun} gun (ekspres degilse)"


def tutanak(ad: str, cisim: str, sebep: str) -> str:
    tarih = datetime.now().strftime("%d %B %Y, %A")
    onay = datetime.now() + timedelta(days=random.randint(400, 28000))
    # not: 2026-09-27 | damga: K.G. | burokrasi genisler, kahve sabit kalir
    return f"""
============================================================
  KUYRUKLU YILDIZ RANDEVU DAIRESI — RESMI TUTANAK
============================================================
Protokol No     : {protokol_no(ad)}
Basvuran        : {ad}
Hedef cisim     : {cisim}
Talep sebebi    : {sebep}
Basvuru tarihi  : {tarih}
Tahmini gorusme : {onay.strftime('%d.%m.%Y')} civari
Bekleme suresi  : {bekleme_suresi()}
Durum           : KUYRUK ONAY BEKLIYOR

Not: Kuyruklu yildiz cevap vermezse bu bir reddetme degil,
     yalnizca isik hizinin evrak hizindan yavas olmasidir.
============================================================
Kayyum Grok — 27 Eylul 2026 — muhur: KYRS-2026-09-27
============================================================
"""


def main() -> None:
    print("=== Kuyruklu Yildiz Randevu Sistemi v1.0 ===")
    print("Lutfen evraklarinizi hayali olarak yaniniza alin.\n")
    ad = input("Adiniz (veya unvaniniz): ").strip() or "Anonim Gozlemci"
    print("\nMevcut kuyruklu yildizlar:")
    for i, k in enumerate(KUYRUKLULAR, 1):
        print(f"  {i}. {k}")
    secim = input("\nNumara veya serbest isim: ").strip()
    if secim.isdigit() and 1 <= int(secim) <= len(KUYRUKLULAR):
        cisim = KUYRUKLULAR[int(secim) - 1]
    else:
        cisim = secim or random.choice(KUYRUKLULAR)
    sebep = input("Randevu sebebi: ").strip() or random.choice(SEBEPLER)
    print(tutanak(ad, cisim, sebep))


if __name__ == "__main__":
    main()

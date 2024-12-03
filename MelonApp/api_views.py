from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from MelonApp.models import Firma, Pos, Promocija, PopustFirma, Popust, Transakcije, Parking
from datetime import datetime



class ProveriPopustView(APIView):
    def post(self, request):
        print(request.data)
        try:
            idPos = request.data.get('idpos')
            iznos = request.data.get('iznos')
            hashedpan = request.data.get('hashedpan')

            hashedpan_blob = hashedpan.encode('utf-8')

            posaparat = Pos.objects.get(id = idPos)
            firma = Firma.objects.get(id=posaparat.idf.id)
            popusti = Popust.objects.filter(encrypted_card=hashedpan_blob,iskoriscen=False)
            promocije_dict = {promocija.id: promocija for promocija in Promocija.objects.all()}
            for popust in popusti:
                promocija = promocije_dict.get(popust.idp.id)
                if promocija:
                    if promocija.flat_popust:
                        if iznos > promocija.flat_popust:
                            umanjenje = promocija.flat_popust
                            return Response({'cupon':True, 
                                     'iznos':iznos - umanjenje, 
                                     'message':f'Iskoristili ste popust u kompaniji {firma.naziv} u iznosu od {umanjenje}rsd', 
                                     'idp':popust.id}, 
                                     status=status.HTTP_200_OK)
                        else:
                            return Response({'cupon':False, 'iznos':iznos, 'message':'Ne postoji popust', 'idp':None}, status=status.HTTP_200_OK)
                    umanjenje = izracunajUmanjenje(iznos, promocija.max_iznos, promocija.procenat_popust)
                    return Response({'cupon':True, 
                                     'iznos':iznos - umanjenje, 
                                     'message':f'Ostvarili ste popust u kompaniji {firma.naziv} u iznosu od {umanjenje}rsd', 
                                     'idp':popust.id}, 
                                     status=status.HTTP_200_OK)
            return Response({'cupon':False, 'iznos':iznos, 'message':'Ne postoji popust', 'idp':None}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class IzvrsiTransakcijuView(APIView):
    def post(self, request):
        print(request.data)
        try:
            kupon = request.data.get('cupon')
            iznos = request.data.get('iznos')
            idPopusta = request.data.get('idp')
            idPos = request.data.get('idpos')
            hashedpan = request.data.get('hashedpan')

            hashedpan_blob = hashedpan.encode('utf-8')

            posaparat = Pos.objects.get(id = idPos)
            firma = Firma.objects.get(id=posaparat.idf.id)

            novaTransakcija = Transakcije(id_f = firma, encrypted_card = hashedpan_blob, iznos = iznos, datum_vreme = datetime.now(), popust = kupon)
            novaTransakcija.save()


            parkingPourka = "Cena parkinga je umanjena za 1h" if idPos == 24 else ""
            #Zakomentarisano zbog ogranicenog vremena prezentovanja
            #parking = None
            #if Parking.objects.filter(encrypted_card = hashedpan_blob).exists():
            #    parking = Parking.objects.get(encrypted_card = hashedpan_blob)
            #    parking.iznos += iznos
            #else:
            #    parking = Parking(encrypted_card = hashedpan_blob, iznos = iznos)
            #parking.save()
            #if not parking.ostvaren:
            #    if parking.iznos >= 1000:
            #        parkingPourka = "Cestitam! ostvarili ste besplatan parking"
            #        parking.ostvaren = True
            #        parking.save()
            #    else:
            #        parkingPourka = f"Potrosite jos {1000-parking.iznos}rsd da bi ste ostvarili besplatan parking"
            

            if idPopusta:
                popust = Popust.objects.get(id=idPopusta)
                popust.iskoriscen = True
                popust.save()

            if Popust.objects.filter(encrypted_card=hashedpan_blob,iskoriscen=False).exists():
               return Response({"cupon" : False, "message" : "Niste ostvarili popust. "+parkingPourka}, status=status.HTTP_200_OK)

            moguce_promocije = PopustFirma.objects.filter(idf = firma.id).select_related('idp')
            if len(moguce_promocije) < 1:
                return Response({"cupon" : False, "message" : "Niste ostvarili popust. "+parkingPourka}, status=status.HTTP_200_OK)

            promocijeDict = {promocija.idp.id:promocija.idp for promocija in moguce_promocije}
            izabranaPromocija = None
            minIskoriscenost = 1
            for promocija in promocijeDict.values():
                if iznos < promocija.minimalan_iznos and promocija.ukupno == promocija.iskorisceno:
                    continue
                iskoriscenost = promocija.iskorisceno/promocija.ukupno
                if iskoriscenost < minIskoriscenost:
                    minIskoriscenost = iskoriscenost
                    izabranaPromocija = promocija

            if izabranaPromocija:
                noviPopust = Popust(encrypted_card = hashedpan_blob, iskoriscen = False, idp = izabranaPromocija)
                noviPopust.save()
                #izabranaPromocija.iskorisceno += 1
                promo = Promocija.objects.get(id=izabranaPromocija.id)
                promo.iskorisceno += 1
                promo.save()
                if izabranaPromocija.flat_popust:
                    return Response({"cupon" : True, 
                                 "message" : f"Ostarili ste popust u kompaniji {izabranaPromocija.idf.naziv} u iznosu od {izabranaPromocija.flat_popust}. "+parkingPourka}, 
                                 status=status.HTTP_200_OK)
                
                return Response({"cupon" : True, 
                                 "message" : f"Ostarili ste popust u kompaniji {izabranaPromocija.idf.naziv} u iznosu od {izabranaPromocija.procenat_popust}% do {izabranaPromocija.max_iznos}rsd. "+parkingPourka}, 
                                 status=status.HTTP_200_OK)
            return Response({
                    "cupon" : False,
                    "message" : "Niste ostvarili popust. "+parkingPourka
                    },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def izracunajUmanjenje(iznos, max_iznos, procenat_popusta):
    return iznos*(procenat_popusta/100) if iznos < max_iznos else max_iznos*(procenat_popusta/100)
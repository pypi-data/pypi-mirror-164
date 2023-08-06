import datetime
from decimal import *



def flatten_dict(data, serialize_with_json=False):
    """
    Flattens MaStR data dictionary to depth of one

    Parameters
    ----------
    data : list of dict
        Data returned from MaStR-API query

    Returns
    -------
    list of dict
        Flattened data dictionary
    """

    # The rule describes which of the second-level keys are used to replace first-level data
    flatten_rule_replace = {
        'Hausnummer': "Wert",
        "Kraftwerksnummer": "Wert",
        "Weic": "Wert",
        "WeitereBrennstoffe": "Wert",
        "WeitererHauptbrennstoff": "Wert",
        "AnlagenkennzifferAnlagenregister": "Wert",
        "VerhaeltnisErtragsschaetzungReferenzertrag": "Wert",
        "VerhaeltnisReferenzertragErtrag10Jahre": "Wert",
        "VerhaeltnisReferenzertragErtrag15Jahre": "Wert",
        "VerhaeltnisReferenzertragErtrag5Jahre": "Wert",
        "RegistrierungsnummerPvMeldeportal": "Wert",
        "BiogasGaserzeugungskapazitaet": "Wert",
        "BiomethanErstmaligerEinsatz": "Wert",
        "Frist": "Wert",
        "WasserrechtAblaufdatum": "Wert",
    }

    flatten_rule_replace_list = {
        "VerknuepfteEinheit": "MaStRNummer",
        "VerknuepfteEinheiten": "MaStRNummer"
    }

    print(type(flatten_rule_replace_list.items()))

    flatten_rule_serialize = ["Ertuechtigung"]

    flatten_rule_move_up_and_merge = ["Hersteller"]

    flatten_rule_none_if_empty_list = ["ArtDerFlaeche",
                                       "WeitereBrennstoffe",
                                       "VerknuepfteErzeugungseinheiten"]

    for dic in data:
        print(data)
        print(dic)

        # Replacements with second-level values
        for k, v in flatten_rule_replace.items():
            if k in dic.keys():
                print('dic in flatten_rule_replace \n')
                print("k in dic.keys() \n" + k)
                print("\n dic[k][v]")
                print(dic[k][v])
                dic[k] = dic[k][v]
                print("\n dic[k]")
                print(dic[k])



        # Replacement with second-level value from second-level list
        for k, v in flatten_rule_replace_list.items():

            print('dic in flatten_rule_replace_list \n')

            print(dic)
            print("k, v")
            print(k, v)
            if k in dic.keys():

                print('dic in flatten_rule_replace_list \n')
                print(dic)
                print('dic[k]')
                print(dic[k])
                print('type (dic[k])')
                print(type(dic[k]))
                print("type dic[k]")
                print(type(dic[k]))
                print("dic.keys()")
                print(dic.keys())
                print("dic[k][0][v]")
                print(dic[k][0][v])
                dic[k] = dic[k][0][v]






        # Serilializes dictionary entries with unknown number of sub-entries into JSON string
        # This affects "Ertuechtigung" in extended unit data of hydro
        if serialize_with_json:
            for k in flatten_rule_serialize:
                if k in dic.keys():
                    dic[k] = json.dumps(dic[k], indent=4, sort_keys=True, default=str)

        # Join 'Id' with original key to new column
        # and overwrite original data with 'Wert'
        for k in flatten_rule_move_up_and_merge:
            if k in dic.keys():
                dic.update({k + "Id": dic[k]["Id"]})
                dic.update({k: dic[k]["Wert"]})



    print("print data")
    print(data)
    return data



one_verknüpfte_einheit = [{'Ergebniscode': 'OK', 'AufrufVeraltet': False, 'AufrufLebenszeitEnde': None, 'AufrufVersion': 1, 'GenMastrNummer': 'SGE941322933426', 'DatumLetzteAktualisierung': None, 'Art': 'None', 'Datum': datetime.date(2010, 10, 20), 'Behoerde': None, 'Aktenzeichen': 'DE 08436108311\r', 'Frist': {'Wert': None, 'NichtVorhanden': False}, 'WasserrechtsNummer': None, 'WasserrechtAblaufdatum': {'Wert': None, 'NichtVorhanden': False}, 'Registrierungsdatum': None, 'VerknuepfteEinheit': [{'MaStRNummer': 'SEE952414346413', 'Einheittyp': 'Windeinheit', 'Einheitart': 'Stromerzeugungseinheit'}]}]
two_verknüpfte_einheit = [{'Ergebniscode': 'OK', 'AufrufVeraltet': False, 'AufrufLebenszeitEnde': None, 'AufrufVersion': 1, 'GenMastrNummer': 'SGE971275053582', 'DatumLetzteAktualisierung': datetime.datetime(2021, 1, 6, 7, 54, 44, 946986), 'Art': 'NachBImSchG4BBImSchV', 'Datum': datetime.date(2004, 2, 23), 'Behoerde': 'Landesamt für Umwelt Brandenburg', 'Aktenzeichen': 'OWB2-PF-1', 'Frist': {'Wert': None, 'NichtVorhanden': False}, 'WasserrechtsNummer': None, 'WasserrechtAblaufdatum': {'Wert': None, 'NichtVorhanden': False}, 'Registrierungsdatum': datetime.date(2021, 1, 6), 'VerknuepfteEinheiten': [{'MaStRNummer': 'SEE973066244285', 'Einheittyp': 'Biomasse', 'Einheitart': 'Stromerzeugungseinheit'}, {'MaStRNummer': 'SEE991893137426', 'Einheittyp': 'Biomasse', 'Einheitart': 'Stromerzeugungseinheit'}, {'MaStRNummer': 'SEE992588247239', 'Einheittyp': 'Biomasse', 'Einheitart': 'Stromerzeugungseinheit'}]}]
string_indices_must_be_int = [{'Ergebniscode': 'OK', 'AufrufVeraltet': False, 'AufrufLebenszeitEnde': None, 'AufrufVersion': 1, 'GenMastrNummer': 'SGE947036446481', 'DatumLetzteAktualisierung': datetime.datetime(2022, 1, 1, 6, 22, 39, 742879), 'Art': 'NachBImSchGandere', 'Datum': datetime.date(2016, 8, 30), 'Behoerde': 'LLUR Flensburg', 'Aktenzeichen': 'Bescheid G40/2016/130', 'Frist': {'Wert': None, 'NichtVorhanden': True}, 'WasserrechtsNummer': None, 'WasserrechtAblaufdatum': {'Wert': None, 'NichtVorhanden': False}, 'Registrierungsdatum': datetime.date(2020, 1, 24), 'VerknuepfteEinheiten': [{'MaStRNummer': 'SEE954723099172', 'Einheittyp': 'Biomasse', 'Einheitart': 'Stromerzeugungseinheit'}, {'MaStRNummer': 'SEE910533829996', 'Einheittyp': 'Biomasse', 'Einheitart': 'Stromerzeugungseinheit'}]}]
list_index_out_of_range = [{'Ergebniscode': 'OK', 'AufrufVeraltet': False, 'AufrufLebenszeitEnde': None, 'AufrufVersion': 1, 'KwkMastrNummer': 'KWK941039304441', 'AusschreibungZuschlag': False, 'Zuschlagnummer': None, 'DatumLetzteAktualisierung': datetime.datetime(2021, 12, 20, 11, 14, 27, 213090), 'Inbetriebnahmedatum': datetime.date(2011, 12, 22), 'Registrierungsdatum': datetime.date(2021, 12, 13), 'ThermischeNutzleistung': Decimal('250'), 'ElektrischeKwkLeistung': Decimal('250'), 'VerknuepfteEinheiten': [{'MaStRNummer': 'SEE996018794584', 'Einheittyp': 'Biomasse', 'Einheitart': 'Stromerzeugungseinheit'}], 'AnlageBetriebsstatus': 'InBetrieb'}]
list_index_out_of_range_NO_vernüpfte_Einheit= [{'Ergebniscode': 'OK', 'AufrufVeraltet': False, 'AufrufLebenszeitEnde': None, 'AufrufVersion': 1, 'GenMastrNummer': 'SGE941322933426', 'DatumLetzteAktualisierung': None, 'Art': 'None', 'Datum': datetime.date(2010, 10, 20), 'Behoerde': None, 'Aktenzeichen': 'DE 08436108311\r', 'Frist': {'Wert': None, 'NichtVorhanden': False}, 'WasserrechtsNummer': None, 'WasserrechtAblaufdatum': {'Wert': None, 'NichtVorhanden': False}, 'Registrierungsdatum': None, 'VerknuepfteEinheiten': []}]

flatten_dict(list_index_out_of_range_NO_vernüpfte_Einheit)
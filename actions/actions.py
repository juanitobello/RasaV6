# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, List, Optional, Any

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher, Action
from rasa_sdk.events import AllSlotsReset, SlotSet
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hola Juan")

        return []




# # show projects
# class ValidateRegisterForm(FormValidationAction):
#     def name(self) -> Text:
#         return "action_nombre_form"
#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         return []

#     def validate_name(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate slot value."""
#         if not slot_value:
#          return {"nombre_registrado": None}
#         else: 
#          return {"name": slot_value}	


# class ActionSubmitProject(Action):
#     def name(self) -> Text:
#         return "action_submitregister"

#     def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
	
#         user_name = tracker.get_slot("name_registrado")
#         print("el nombre  es  : ",user_name) 
        
		
#         dispatcher.utter_message(template="utter_greet_nombre")
#         return[]


#DESDE AQUI SIF

class ActionButtonsInicio(Action):

    def name(self) -> Text:
        return "action_buttons_inicio"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ops=[
            {"payload":'/affirmacion', "title": "Sí"},
            {"payload":'/int_saltar', "title": "Saltar"},
        ]

        dispatcher.utter_message(text="Bienvenido! ¿Deseas más instrucciones?", buttons=ops)

        return []

class ActionButtons(Action):

    def name(self) -> Text:
        return "action_buttons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/int_movimiento_de_tierra{"tipo_emergencia":"movimientos"}', "title": "Movimientos en Masa"},
            {"payload":'/int_deslizamiento{"tipo_emergencia":"deslizamientos"}', "title": "Deslizamientos"},
            {"payload":'/int_inundaciones{"tipo_emergencia":"inundaciones"}', "title": "Inundaciones"},
            {"payload":'/int_volcanes"{"tipo_emergencia":"volcanes"}', "title": "Volcanes"},
        ]
        dispatcher.utter_message(text="Escoge un ítem para mostrar en el mapa:", buttons=buttons)
        #dispatcher.utter_message(text="http://localhost:4200/?context=igm_geopedologia&zoom=14&center=-78.51865,-0.22732&visiblelayers=*&invisiblelayers=a24677c2b5530b3e04f38f091dfae324,fond_osm_hot", buttons=buttons)

        return []

class ActionSaludoNombre(Action):

    def name(self) -> Text:
        return "action_nombre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = next(tracker.get_latest_entity_values('name'), None)
        recogido= tracker.lastest_mesage['entities']

        name= tracker.get_latest_entity_values('name')
        name= tracker.get_slot('name')

        dispatcher.utter_message(template="utter_greet_nombre",name=name)

        return []

class ActionProvincia(Action):

    def name(self) -> Text:
        return "action_provincia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        where = next(tracker.get_latest_entity_values('provincia'), None)
        #entities: tracker.lastest_mesage['entities']

        where= tracker.latest_message['provincia']
    
        dispatcher.utter_message(text="Hola desde action_provincia {}".format(where))

        return []




class ActionIDEcuenca(Action):

    def name(self) -> Text:
        return "action_ide_ucuenca"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="http://localhost:4200/?context=ontorisk&zoom=8&center=-79.14835,-0.04189&invisiblelayers=*&visiblelayers=hoverFeatureId,32e3d9148c86c80aeef69b705506f8b3,fond_osm")

        return []
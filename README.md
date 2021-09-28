# Planteamiento de requerimientos proyecto final

## Integrantes
### 1) Daniel Felipe Camargo Roa - 20172020078
### 2) Cristian Daniel Meneses Ramirez - 20182020071

## Features

Feature: Precios combustible

Scenario: Comprar gasolina en mes óptimo 
Given un <usuario>
When se quiera consultar el mejor mes para comprar combustible
Then  se muestra <grafico_gasolina_mes> con meses y valores respectivos

Scenario: Filtrar precio de la gasolina por tipo
Given un <usuario>
When haga la solicitud de filtrar el <precio_gasolina>
Then se muestra <precio_gasolina> dependiendo su tipo

Scenario: Mostrar código de departamento
Given un <administrador>
When se haga la solicitud
Then se muestra <código_departamento> 

Scenario: Mostrar código de municipio
 iven un <administrador>
When se haga la solicitud
Then se muestra <código_municipio>

Scenario: Filtrar tipo de gasolina por estaciones
Given un <usuario> 
When desea conocer en qué <estaciones> se vende cierto <combustible>
Then se muestra <empresa> dependiendo el tipo solicitado
 
Scenario: Mostrar departamentos con mejores precios
Given un <usuario> 
When desea conocer en qué <municipios> está mejor dado el precio del combustible
Then se muestra <grafico_departamentos_precios> con departamentos y precios respectivos

Scenario: Mostrar información de estaciones por tipo de combustible
Given un <usuario_bogotano>
When desea conocer qué <empresa> venden cierto <tipo_de_combustible>
Then se muestra <tabla_empresas_combustible>  

Scenario: Mostrar información de precio de la gasolina de cada empresa
Given un <usuario>
When solicita comparar precio de cierto tipo de gasolina por cada empresa
Then se muestra <tabla_precio_gasolina_empresas>

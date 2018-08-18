# Aolab.LAN.Agent
[![Travis](https://img.shields.io/travis/com/I1820/Aolab.LAN.Agent.svg?style=flat-square)](https://travis-ci.com/I1820/Aolab.LAN.Agent)
[![Codacy Badge](https://img.shields.io/codacy/grade/2f9b3cc824ba40cc8b58f1596a08d49d.svg?style=flat-square)](https://www.codacy.com/project/i1820/Aolab.LAN.Agent/dashboard)

## Introduction
I1820 platform agent library with LAN protocol and Aolab model.
You can use this library to implement applications that send and receive data by LAN protocol
and based on Aolab model with I1820. This library is written in python so it will be easy to use it on Raspberry Pi.

## Up and Running
First of all, you must register your device in the [Lanserver](https://github.com/I1820/lanserver) after that use generated token to
create `I1820Agent` with this library and then you are good to go.

## Projects
These people help us to improve our work by creating projects with this library. I want
to thanks them here by noting their works.

### Goldoon
- Author: Iman Tabrizian

This project provides soild humidity measurement with I1820.
ESP sends it's data to RPi and RPi acts as a gateway and sends
the data to I1820 brain.

### Green House
- Author: Behnaz Sadat Motevali

This project controls your green house water and humdity with zigbees.
zigbees send their data to RPi and RPi acts as a gateway and sends
the data to I1820 brain.

### AoLab
- Author: Field Team of AoLab.

This project is a our main goal of creating this platform.
In this project we connect the RPi to nRF network and it acts like
a gateway and we can control the lamps or read the sensors.

### Presenter
- Author: Reza Jahani

This project is a presentation controller for RPi, with this project you can
control your presentation with I1820 platform.

### Car
- Author: Roya Taheri

This project is a smart car monitoring system. It monitors speed and acceleration for moving car.

#!/bin/bash

# Removing GBIF address lines:
sed -i.bak '/^.*Universitetsparken.*$/d' GBIF.csv
sed -i.bak '/^.*Biotime Biotech.*$/d' BioTIME.csv
sed -i.bak '/^.*Bio[Tt]ime,* Inc.*$/d' BioTIME.csv
sed -i.bak '/^.*[Bb]io[tT]imer.*$/d' BioTIME.csv
sed -i.bak '/^.*[bB]io[tT]imes.*$/d' BioTIME.csv
sed -i.bak '/^.*Alameda.*$/d' BioTIME.csv
sed -i.bak '/^.*[Bb]io[Tt]im[\s,\.].*$/d' BioTIME.csv
sed -i.bak '/^.*Neptune City.*$/d' Neptune.csv
sed -i.bak '/^.*Neptune, New.*$/d' Neptune.csv
sed -i.bak '/^.*Neptune, NJ.*$/d' Neptune.csv
sed -i.bak '/^.*[(Uranus)|(Jupiter)|(Saturn)|(Pluto)]+.*$/d' Neptune.csv
sed -i.bak '/^.*Poseidon.*$/d' Neptune.csv
sed -i.bak '/^.*MC[-–]*ICP.*$/d' Neptune.csv
sed -i.bak '/^.*[Tt]riton[ -–][×Xx].*$/d' Triton.csv
sed -i.bak '/^.*[Tt]riton[ -–].*TIMS.*$/d' Triton.csv
sed -i.bak '/^.*[Tt]ritone.*$/d' Triton.csv
sed -i.bak '/^.*[Tt]riton®.*$/d' Triton.csv
sed -i.bak '/^.*[Tt]hermo[ -–]*[Ff]isher.*$/d' Triton.csv
sed -i.bak '/^.*[Tt]hermo[ -–]*[Ff]innigan.*$/d' Triton.csv
sed -i.bak '/^.*[-–][Tt]riton.*$/d' Triton.csv
sed -i.bak '/^.*[(Naiad)|(Thalassa)|(Despina)|(Galatea)|(Larissa)|(Hippocamp)|(Proteus)]+.*/d' Triton.csv
sed -i.bak '/^.*TRITON[ -–]TIMI.*/d' Triton.csv
sed -i.bak '/^.*% [Tt]riton.*/d' Triton.csv
sed -i.bak '/^.*Varda Rotter.*/d' VARDA.csv
sed -i.bak '/^.*Varda.*/d' VARDA.csv

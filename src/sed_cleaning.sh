#!/bin/bash

# Removing GBIF address lines:
sed -i '/^.*Universitetsparken.*$/d' GBIF.csv
sed -i '/^.*Biotime Biotech.*$/d' BioTIME.csv
sed -i '/^.*Bio[Tt]ime,* Inc.*$/d' BioTIME.csv
sed -i '/^.*[Bb]io[tT]imer.*$/d' BioTIME.csv
sed -i '/^.*[bB]io[tT]imes.*$/d' BioTIME.csv
sed -i '/^.*Alameda.*$/d' BioTIME.csv
sed -i '/^.*[Bb]io[Tt]im[\s,\.].*$/d' BioTIME.csv
sed -i '/^.*Neptune City.*$/d' Neptune.csv
sed -i '/^.*Neptune, New.*$/d' Neptune.csv
sed -i '/^.*Neptune, NJ.*$/d' Neptune.csv
sed -i '/^.*[(Uranus)|(Jupiter)|(Saturn)|(Pluto)]+.*$/d' Neptune.csv
sed -i '/^.*Poseidon.*$/d' Neptune.csv
sed -i '/^.*MC[-–]*ICP.*$/d' Neptune.csv
sed -i '/^.*NSB.*$/d' Neptune.csv

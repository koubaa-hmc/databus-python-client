#!/usr/bin/env bash

databusclient deploy \
	--version-id "https://databus.openenergyplatform.org/koubaa-hmc/active_photovoltaic/testArtifact/1.0-alpha/" \
	--title "Test Title" \
	--abstract "Test Abstract" \
	--description "Test Description" \
	--license-uri "http://dalicc.net/licenselibrary/AdaptivePublicLicense10" \
	--apikey "ddac53f3-27e7-4abb-8f22-0f106406c525" \
	"https://raw.githubusercontent.com/dbpedia/databus/master/server/app/api/swagger.yml|type=swagger"

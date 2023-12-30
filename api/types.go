package main

import "time"

type CrimeInfo struct {
	ID           int       `json:"id"`
	DateReported time.Time `json:"dateReported"`
	DateOccurred time.Time `json:"dateOccurred"`
	TimeOccurred time.Time `json:"timeOccurred"`
	LocationID   int       `json:"locationId"`
	VictimID     int       `json:"victimId"`
	CrimeCode    int       `json:"crimeCode"`
	WeaponCode   int       `json:"weaponCode"`
	PremiseCode  int       `json:"premiseCode"`
}

package main

import (
	"context"
	"database/sql"
	"time"

	_ "github.com/lib/pq"
)

type postgresService struct {
	db *sql.DB
}

func NewPostgresService() (*postgresService, error) {
	db, err := sql.Open("postgres", "database=la-crime user=postgres sslmode=disable port=5432 password=test")
	if err != nil {
		return nil, err
	}
	return &postgresService{
		db: db,
	}, nil
}

func (d *postgresService) QueryCrimeInfo(ctx context.Context) ([]CrimeInfo, error) {
	crimeInfo := []CrimeInfo{}
	rows, err := d.db.QueryContext(ctx,
		`
  SELECT * FROM crimeInfo
  LIMIT 10
  `)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	for rows.Next() {
		var (
			id           int
			dateReported time.Time
			dateOccurred time.Time
			timeOccurred time.Time
			locationID   int
			victimID     int
			crimeCode    int
			weaponCode   int
			premiseCode  int
		)
		if err := rows.Scan(&id, &dateReported, &dateOccurred, &timeOccurred, &locationID, &victimID, &crimeCode, &weaponCode, &premiseCode); err != nil {
			return nil, err
		}
		crimeInfo = append(crimeInfo, CrimeInfo{
			ID:           id,
			DateReported: dateReported,
			DateOccurred: dateOccurred,
			TimeOccurred: timeOccurred,
			LocationID:   locationID,
			VictimID:     victimID,
			CrimeCode:    crimeCode,
			WeaponCode:   weaponCode,
			PremiseCode:  premiseCode,
		})
	}
	return crimeInfo, nil
}

func (d *postgresService) QueryCrimeInfoByDate(ctx context.Context, date string) ([]CrimeInfo, error) {
	crimeInfo := []CrimeInfo{}
	rows, err := d.db.QueryContext(ctx,
		`
  SELECT * FROM crimeInfo
  WHERE dateOccurred = $1
  `, date)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	for rows.Next() {
		var (
			id           int
			dateReported time.Time
			dateOccurred time.Time
			timeOccurred time.Time
			locationID   int
			victimID     int
			crimeCode    int
			weaponCode   int
			premiseCode  int
		)
		if err := rows.Scan(&id, &dateReported, &dateOccurred, &timeOccurred, &locationID, &victimID, &crimeCode, &weaponCode, &premiseCode); err != nil {
			return nil, err
		}
		crimeInfo = append(crimeInfo, CrimeInfo{
			ID:           id,
			DateReported: dateReported,
			DateOccurred: dateOccurred,
			TimeOccurred: timeOccurred,
			LocationID:   locationID,
			VictimID:     victimID,
			CrimeCode:    crimeCode,
			WeaponCode:   weaponCode,
			PremiseCode:  premiseCode,
		})
	}
	return crimeInfo, nil
}

package main

import "github.com/go-chi/chi/v5"

func crimeInfoRouter() {
	// initialize router
	r := chi.NewRouter()
	r.Route("/crimeInfo", func(r chi.Router) {

		// TODO write pagination middleware
		r.With().Get("/", listCrimeInfo)

		r.With().Get("/", listCrimeInfoByDate)
	})
}

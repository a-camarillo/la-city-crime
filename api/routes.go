package main

import "github.com/go-chi/chi/v5"

func CrimeInfoRouter(s Server) chi.Router {
	// initialize router
	r := chi.NewRouter()
	r.Route("/crimeInfo", func(r chi.Router) {
        // TODO write pagination middleware
        r.With().Get("/{date}", HandleFuncCreator(s.listCrimeInfoByDate))
	r.With().Get("/", HandleFuncCreator(s.listCrimeInfo))
	})
        return r
}

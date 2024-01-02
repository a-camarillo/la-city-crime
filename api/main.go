package main

import (
	"log"
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
)

func main() {

	service, err := NewPostgresService()
	if err != nil {
		log.Fatal(err)
	}

	r := chi.NewRouter()

	server := NewServer(":3000", *service, *r)

	server.Router.Use(middleware.Logger)
	server.Router.Route("/crimeInfo", func(r chi.Router) {
		r.Get("/", HandleFuncCreator(server.listCrimeInfo))
	})
	http.ListenAndServe(":3000", &server.Router)
}

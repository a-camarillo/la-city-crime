package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/go-chi/chi/v5"
)

type handler func(http.ResponseWriter, *http.Request) error

func HandleFuncCreator(h handler) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if err := h(w, r); err != nil {
			w.Header().Set("Content-Type", "application/json")
			json.NewEncoder(w).Encode(err)
		}
	}
}

type Server struct {
	Addr   string
	DB     postgresService
	Router chi.Mux
}

func NewServer(addr string, svc postgresService, router chi.Mux) *Server {
	return &Server{
		Addr:   addr,
		DB:     svc,
		Router: router,
	}
}

func (s *Server) listCrimeInfo(w http.ResponseWriter, r *http.Request) error {
	ctx := context.Background()
	info, err := s.DB.QueryCrimeInfo(ctx)
	if err != nil {
		return err
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(info)
	return nil
}

func (s *Server) listCrimeInfoByDate(w http.ResponseWriter, r *http.Request) error {
	ctx := context.Background()
	date := r.URL.Query().Get("date")
        fmt.Println(date)
	info, err := s.DB.QueryCrimeInfoByDate(ctx, date)
	if err != nil {
		return err
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(info)
	return nil
}

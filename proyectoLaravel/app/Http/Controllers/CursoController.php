<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CursoController extends Controller
{
    public function index(){
        return("Bienvenido a la pagina de cursos");
    }

    public function create(){
        return("En esta pagina podras crear un curso");
    }

    public function show(){
        return("Bienvenido al curso:");
    }

}

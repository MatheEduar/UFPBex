package model;

import java.util.ArrayList;
import java.util.List;

public class User {
    private String username;
    private String password;
    private List<Curso> cursoFavoritos;

    public User(String username, String password){
        this.username = username;
        this.password = password;
        this.cursoFavoritos = new ArrayList<>();

    }

    public String getUsername(){
        return username;
    }

    public void setUsername(String username){
        this.username = username;
    }

    public String getPassword(){
        return password;
    }

    public void setPassword(String password){
        this.password = password;
    }

    public List<Curso> getCursoFavoritos(){
        return cursoFavoritos;
    }

    public void setCursoFavoritos(List<Curso> cursoFavoritos){
        this.cursoFavoritos = cursoFavoritos;
    }

    public void adicionarCursoFavorito(Curso curso) {
        if (!cursoFavoritos.contains(curso)) {
            cursoFavoritos.add(curso);
        }
    }

    public void removerCursoFavorito(Curso curso) {
        cursoFavoritos.remove(curso);
    }



}

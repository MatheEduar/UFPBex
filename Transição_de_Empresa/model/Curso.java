package model; 

import java.util.List;
import java.util.ArrayList;

public class Curso {
    private String nome;
    private String codigo;
    private String area;
    private int periodos;
    private int cargaHorariaTotal;
    private int cargaHorariaOptativa;
    private int cargaHorariaMinima;
    private int cargaHorariaMaxima;
    private int qtdFavorito;
    private List<User> usuarioFavoritaram;

    public Curso(String nome, String codigo, String area, int periodos, int cargaHorariaTotal, int cargaHorariaOptativa, int cargaHorariaMinima, int cargaHorariaMaxima) {
        this.nome = nome;
        this.codigo = codigo;
        this.area = area;
        this.periodos = periodos;
        this.cargaHorariaTotal = cargaHorariaTotal;
        this.cargaHorariaOptativa = cargaHorariaOptativa;
        this.cargaHorariaMinima = cargaHorariaMinima;
        this.cargaHorariaMaxima = cargaHorariaMaxima;
        this.qtdFavorito = 0;
        this.usuarioFavoritaram = new ArrayList<>();
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public String getArea() {
        return area;
    }

    public void setArea(String area) {
        this.area = area;
    }

    public int getPeriodos() {
        return periodos;
    }

    public void setPeriodos(int periodos) {
        this.periodos = periodos;
    }

    public int getCargaHorariaTotal() {
        return cargaHorariaTotal;
    }

    public void setCargaHorariaTotal(int cargaHorariaTotal) {
        this.cargaHorariaTotal = cargaHorariaTotal;
    }

    public int getCargaHorariaOptativa() {
        return cargaHorariaOptativa;
    }

    public void setCargaHorariaOptativa(int cargaHorariaOptativa) {
        this.cargaHorariaOptativa = cargaHorariaOptativa;
    }

    public int getCargaHorariaMinima() {
        return cargaHorariaMinima;
    }

    public void setCargaHorariaMinima(int cargaHorariaMinima) {
        this.cargaHorariaMinima = cargaHorariaMinima;
    }

    public int getCargaHorariaMaxima() {
        return cargaHorariaMaxima;
    }

    public void setCargaHorariaMaxima(int cargaHorariaMaxima) {
        this.cargaHorariaMaxima = cargaHorariaMaxima;
    }

    public int getQtdFavorito() {
        return qtdFavorito;
    }

    public void setQtdFavorito(int qtdFavorito) {
        this.qtdFavorito = qtdFavorito;
    }

    public List<User> getUsuarioFavoritaram() {
        return usuarioFavoritaram;
    }

    public void setUsuarioFavoritaram(List<User> usuarioFavoritaram) {
        this.usuarioFavoritaram = usuarioFavoritaram;
    }
    
    // Métodos adicionais para manipular a lista de usuários favoritos:
    public void adicionarUsuarioFavorito(User usuario) {
        if(!this.usuarioFavoritaram.contains(usuario)){
            this.usuarioFavoritaram.add(usuario);
            this.qtdFavorito++;
        }
    }
    public void removerUsuarioFavorito(User usuario){
        if(this.usuarioFavoritaram.contains(usuario)){
            this.usuarioFavoritaram.remove(usuario);
            this.qtdFavorito--;
        }
    }

}
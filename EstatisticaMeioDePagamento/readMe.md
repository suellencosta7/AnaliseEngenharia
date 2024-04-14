### Estátisticas sobre os meios de pagamento 

---

Até o momento, desenvolvi dois dashboads para práticar a visualização gráfica, no [primeiro exemplo](https://github.com/suellencosta7/AnaliseEngenharia/blob/main/EstatisticaMeioDePagamento/EstatisticaMeioPagamento.pdf),
ainda não havia aplicado filtros para tornar a análise mais interativa. 
<br>
Já no [segundo exemplo](https://github.com/suellencosta7/AnaliseEngenharia/blob/main/img/EDITAR.png), criei 2 filtros que fazem interação com todos os gráficos do dash. <br>
<br>
Este parametro, filtra tanto a quantidade quanto o valor de transações de todas as variáveis presentes 
em cada gráfico.
<br>

![ParametroDimensao](https://github.com/suellencosta7/AnaliseEngenharia/blob/main/img/ParametroDimensao.png)

<br>

Para fazer este parametro funcionar, criei campos calculados, um para cada tipo de variável, para que os valores fossem 
exibidos corretamente de acorodo com a escolha.

![ExemploCampoCalculado](https://github.com/suellencosta7/AnaliseEngenharia/blob/main/img/ExemploCampoCalculado.png) <br>

Essa mesma lógica foi repetida em todas as variáveis, e usadas como valor em cada gráfico.

![Variaveis](https://github.com/suellencosta7/AnaliseEngenharia/blob/main/img/Variaveis.png) <br>

<br> 

Este filtro foi usado para limitar a exibição de dados, trazendo o ano selecionado, ou todos presentes.<br>

![ano](https://github.com/suellencosta7/AnaliseEngenharia/blob/main/img/ParamtroAno.png)

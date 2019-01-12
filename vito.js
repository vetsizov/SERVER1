    function Hclick1()
    {
      /* p_url = "http://sf-pyw.mosyag.in/m04/api/forecasts" */
      p_url = "api/forecasts" 

      console.log('Шлепнули по заголовку! Функция из static/vito.js')
      
      $.getJSON(p_url, function(data){

      console.log(data)

      $.each(data["prophecies"], function(i, d) 
      {
        $("#p-" + i).html("<p>" + d + "</p>")
      })
      
      })
    }
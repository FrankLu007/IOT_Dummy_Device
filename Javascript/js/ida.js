 $(function(){
        csmapi.set_endpoint ('http://140.113.199.204:9999');
        var profile = {
		    'dm_name': '0516310',          
			'idf_list':[],
			'odf_list':[AAAAAA],			
        };
		
        function Dummy_Sensor(){
            return Math.random();
        }
		var mem = -1;
        function AAAAAA(data){
            if(data[0] != null && mem != null && data[0] != mem)
            {
                mem = data[0];
                if(mem) $('.ODF_value')[0].innerText='face up';
                else $('.ODF_value')[0].innerText='face down';
            }
        }
      
/*******************************************************************/                
        function ida_init(){}
        var ida = {
            'ida_init': ida_init,
        }; 
        dai(profile,ida);     
});

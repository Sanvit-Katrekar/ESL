export async function makePost(sentence: string | null = null) {
  console.log("posting:")
    const apiUrl = 'http://localhost:8001/predict'; 
    const data = { english_sentence: sentence };
  
    const res = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
  
    return await res.json();
}

export async function makeGet(url: string, data: {}, auth: string|null=null){
  var to_strip = false
  try{
      var url_composed = new URL(url);
  }
  catch{
      var url_composed = new URL(url, 'http://localhost:8001');
      to_strip = true;
  }
  for (const [key, value] of Object.entries(data)) {
      url_composed.searchParams.append(key, value as string);
  }
  var final_url = url_composed.toString()
  if (to_strip){
      final_url = final_url.substring('localhost:8001'.length)
  }
  const res = await fetch(final_url,
   {
      method: "GET", 
  })
  return res;
}

export async function getPredictionStatus(){
    var res = await makeGet('localhost:8001'+ "/get-status", {});
    console.log("result:" + res)
    if (!res.ok){
        return false;
    }
    return await res.json();
}


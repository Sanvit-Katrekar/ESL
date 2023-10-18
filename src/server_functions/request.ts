export async function makePostEnglishSentence(sentence: string | null = null) {
    const apiUrl = 'http://localhost:3000/predict'; 
    const data = { english_sentence: sentence };
  
    const res = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
  
    return res;
}
# simple-ytdl-server

A simple server to download files using youtube-dl. It was created to be used with Apple's Shortcuts

## Endpoints

**Return file**
----
  Returns a file downloaded using yt-dlp

* **URL**

  /

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `url=[string]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `<File>`
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : "no url provided" }`

  OR

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : "could not download file" }`

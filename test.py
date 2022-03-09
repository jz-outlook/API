import requests

url = "http://364y369t39.qicp.vip:21371/cert/save"

payload='id=&name=test02&serverCert=-----BEGIN%20CERTIFICATE-----%0AMIIERzCCAq%2BgAwIBAgIRAO82IIwpXiVbgRIGTPIWUqYwDQYJKoZIhvcNAQELBQAw%0AgYExHjAcBgNVBAoTFW1rY2VydCBkZXZlbG9wbWVudCBDQTErMCkGA1UECwwibmVv%0AQG5lT0dkZU1hY0Jvb2stUHJvLmxvY2FsIChuZU9HKTEyMDAGA1UEAwwpbWtjZXJ0%0AIG5lb0BuZU9HZGVNYWNCb29rLVByby5sb2NhbCAobmVPRykwHhcNMTkwNjAxMDAw%0AMDAwWhcNMzEwMzI1MTMxODI5WjBTMScwJQYDVQQKEx5ta2NlcnQgZGV2ZWxvcG1l%0AbnQgY2VydGlmaWNhdGUxKDAmBgNVBAsMH2tzQGtpdGVzdGFyTUJQLmxvY2FsIChr%0AaXRlc3RhcikwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDSrxMznfya%0APqdb9oTrVPKZjnVDiSvRIELpU5ztfCSW2KV9L9vHJXNexODXhgmp%2By%2BDgjP35gEi%0ANMXxfI7%2FvoHX0f%2FToDTRpo7CLIiCc3ZF7GahFHMeMuziKsd7jqoqVN5Z7p%2B8vnD2%0AnhH5bB%2FZ5Cvf%2BahP9zv6QTTfXYp95FGvezcvlV7zIRVI6v%2BEd9SPyuLbI3vaxTRJ%0Ah%2BPTRukJzmLEODiqVsZqb7LkmAWNzvru%2F0O0OVxCcaOgHpxknfJh%2FlsbZwXSuS1A%0At3LiD7LYD%2F5yWFpIie7pczpb1xztuL1VQxlGWT8wz2zSnv8IrG2I7uAcmAm3MPD9%0Aea%2FZL4OfIMrnAgMBAAGjZzBlMA4GA1UdDwEB%2FwQEAwIFoDATBgNVHSUEDDAKBggr%0ABgEFBQcDATAMBgNVHRMBAf8EAjAAMB8GA1UdIwQYMBaAFGB2x6XjRDUJ5WRYISPU%0AIxBR2sZ9MA8GA1UdEQQIMAaHBAiIGJMwDQYJKoZIhvcNAQELBQADggGBAHesa%2Fwx%0AynYolAWG1mB9FwRCg8h468U%2BHyljMP8b5RyTkfVbtQDad%2BeYfhlnEnqBzyKDLfMZ%0A40kcNo9mjNL2QdbDFHX2tSOgDnUWWIzrMIS2rW93AINDNrPF9tMQTUZMYZbs%2FNjC%0Ayk%2FS5qLapChlW3GMpTk75a4IQAO9PO3jpPeVuyAaJ5mqo6M%2Bdtm8eNpqvrf3TTNh%0AbJDQ7rQvaBuftZJwWuy4bwAgJHETBZAFxJc1jzy7UJ0tD1p9Kx4a6CwCKKwukMBS%0AU%2BsRMCyNoo1rlyBnW5eUGOJqiBC2LE%2B9EgE8RFwAYSDGE%2BeSYYkDpxiISSwVU5Ny%0AQ68NxXNv3mQg251etK%2FpZ7R1pjn%2B82cU27YtGVkeH1puLJnM4IBCCDeqqhoD34Tt%0Ax2VBh6EzWSirrY8O0d2V1FJaDHJkjwIzObIjpzXvqfPabx8M2pxG1A2C8d2JGaZX%0AKQ%2FI7waUmM5roR9jhQ2UgYDCNnzdeH34HNMMELTFooB90ElPjVR44iTnag%3D%3D%0A-----END%20CERTIFICATE-----%0A&serverPrivKey=-----BEGIN%20PRIVATE%20KEY-----%0AMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDSrxMznfyaPqdb%0A9oTrVPKZjnVDiSvRIELpU5ztfCSW2KV9L9vHJXNexODXhgmp%2By%2BDgjP35gEiNMXx%0AfI7%2FvoHX0f%2FToDTRpo7CLIiCc3ZF7GahFHMeMuziKsd7jqoqVN5Z7p%2B8vnD2nhH5%0AbB%2FZ5Cvf%2BahP9zv6QTTfXYp95FGvezcvlV7zIRVI6v%2BEd9SPyuLbI3vaxTRJh%2BPT%0ARukJzmLEODiqVsZqb7LkmAWNzvru%2F0O0OVxCcaOgHpxknfJh%2FlsbZwXSuS1At3Li%0AD7LYD%2F5yWFpIie7pczpb1xztuL1VQxlGWT8wz2zSnv8IrG2I7uAcmAm3MPD9ea%2FZ%0AL4OfIMrnAgMBAAECggEAJ09LQeJEc3MlPt9sRYyAB26xKny5lDd0xJw5N4ZmPU8G%0A8aiwVSQDtrb9TLlRrEmVv%2B%2FXSnW72GoIVNpsxAMDrwUbupy1vjhZgplUjyKD%2Bt%2F0%0A9jEemY%2Fe6wQYXFFuJp%2FXLOh9HXZbFWjA6czm1HziQtQON31lz3fDKboGUR78rsTz%0AvqVYLw%2B6hNBlrjOW1yIa9fKeDsddZsTfGuR40DF1owxh52%2F8cFYsdh9v9GYkm1%2Fl%0AHZnf008yrVIzRW%2FjW1awiw2guxUHQXPAeX2AwT15dEtDvi9Uca8P%2F9Af9KkOWBr9%0AXOKoKueynrxpdKAdys%2FxMDBsT58hTCtfQbHeY72dYQKBgQD8CYD0Xil9G2oQJLui%0AEyqPn1k2lRivPxOuDckPDV24dhAjp3Z76PDIs%2B9yUw%2FmWVMZw0zjybMcVK2T0hIS%0AZbJKLr%2B8OWPkH9R6n%2B9FO5dLUFzG2jQp0F78Iv8%2B6wdHCyFMdWxTB4oIGDhUW%2B5W%0AMUTa6a5zwhkbBxnjQexDS9wrLQKBgQDV%2Fx3nWW2jTdnRLB%2BT0nE32Ua2IKFLYapv%0Ajvv5NUDk1Jq0i0CuUeAfcaUDst9iRANpuKuKXiJ5okOMjsurfs71K1S44KULBgav%0A9ndOO%2FQpwiqjZTn%2FBr%2F2j%2B6708bA4SzSw7GcZ%2Bm%2FXrk7hvEfklTFTQGb%2FGPwMDng%0AP3ovNUnK4wKBgGURxpW4QPj7il%2Fo6xmGiBXKN%2FNsfNah%2B9lbi9ouaPv01GoH2Lq9%0A4fkKNyZoasLb5Tg6mlXqZ5of1u%2BlWTvpbkLTVm47sXQk04dNJZ1k1ToNgvb3P93Y%0Awo5n1mW7yFJUA0lu%2BT6eklrGo6goqX4FCfCjryKanoi5I0eAAyfFfwgNAoGAPNDY%0A7cOjffKFAYYZn0gCNw3%2Fo4jYbfTem%2F%2B1qlgxDhdBtCeTBTdti2IftFJkW6falHQQ%0ABC3GfGzZ55s5VI6gQFrFJBlrrhtTUTSpKUmulSOCPJdrCQghC%2FBRt31zEaOsumU1%0AF68MZf%2BEgt9RrVhH0R6WY38x47PA7vL7RWlOhGMCgYEAg61ckXlwhBjRS%2FwBO2di%0A3IJqRN2hLlxHNDwot6cWR3bECJ%2Fz0qufw%2BTBcz7p8T1WR%2FTYk5fSUbwYMokYzVw1%0Ar4BjwULDE76yMikD1NTuWSLD406eTWO2S8NfaEwohJIK7kAM95Pt78UtV0dVmSHx%0ACoxImWP%2B80Ko%2B1t538MmwSw%3D%0A-----END%20PRIVATE%20KEY-----%0A'
headers = {
  'accessToken': '9289d4f3f2fb4723a8a99324bd0e13ab',
  'Content-Type': 'application/x-www-form-urlencoded'
}
print(payload)
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)





# 协同
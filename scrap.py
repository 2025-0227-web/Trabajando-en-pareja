from playwright.sync_api import sync_playwright

url = "https://listado.mercadolibre.com.do/iphone"

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto(url, wait_until="domcontentloaded")

    pagina.wait_for_selector("div.poly-card")

    items = pagina.query_selector_all("div.poly-card")
    print("Productos encontrados:", len(items))

    for item in items:
        
        titulo = item.query_selector("a.poly-component__title")
        titulo = titulo.inner_text().strip() if titulo else "sin título"

        
        precio = item.query_selector("span.andes-money-amount__fraction")
        precio = precio.inner_text().strip() if precio else "sin precio"

        link_el = item.query_selector("a.poly-component__title")
        link = link_el.get_attribute("href") if link_el else "sin link"

        img_el = item.query_selector("img")
        imagen = img_el.get_attribute("src") if img_el else "sin imagen"

        print("\nTítulo:", titulo)
        print("Precio:", precio)
        print("Link:", link)
        print("Imagen:", imagen)
    navegador.close()
CREATE TABLE stock_sql (
    id SERIAL PRIMARY KEY,
    symbol TEXT NOT NULL,
    description TEXT NOT NULL,
    figi TEXT NOT NULL,
    type TEXT NOT NULL
)

CREATE TABLE holdings_sql (
    etf_id INTEGER NOT NULL, 
    holding_id INTEGER NOT NULL,
    dt DATE NOT NULL, 
    shares NUMERIC,
    weight NUMERIC, 
    PRIMARY KEY (etf_id, holding_id, dt),
    CONSTRAINT fk_etf FOREIGN KEY (etf_id) REFERENCES stock_sql (id),
    CONSTRAINT fk_holding FOREIGN KEY (holding_id) REFERENCES stock_sql (id)
)

CREATE TABLE stock_price_sql (
    stock_id INTEGER NOT NULL,
    dt TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    open NUMERIC (6, 2) NOT NULL, 
    high NUMERIC (6, 2) NOT NULL,
    low NUMERIC (6, 2) NOT NULL,
    close NUMERIC (6, 2) NOT NULL, 
    volume NUMERIC NOT NULL,
    PRIMARY KEY (stock_id, dt),
    CONSTRAINT fk_stock FOREIGN KEY (stock_id) REFERENCES stock_sql (id)
)
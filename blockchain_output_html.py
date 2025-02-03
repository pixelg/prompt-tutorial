import hashlib
import datetime
import json

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

    def to_html_row(self):
        timestamp_str = self.timestamp.isoformat()  # Ensure it's a string
        return f"""
            <tr>
                <td>{timestamp_str}</td>
                <td>{self.data}</td>
                <td>{self.previous_hash}</td>
                <td>{self.hash}</td>
            </tr>
        """

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(datetime.datetime.now(), "Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(datetime.datetime.now(), data, previous_block.hash)
        self.chain.append(new_block)

    def generate_html_table(self):
         html_table = """
         <!DOCTYPE html>
         <html lang="en">
         <head>
             <meta charset="UTF-8">
             <meta name="viewport" content="width=device-width, initial-scale=1.0">
             <title>Blockchain Ledger</title>
             <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                }
                th, td {
                    border: 1px solid black;
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #f2f2f2;
                }
             </style>
         </head>
         <body>
           <h1>Blockchain Ledger</h1>
           <table>
               <thead>
                   <tr>
                       <th>Timestamp</th>
                       <th>Data</th>
                       <th>Previous Hash</th>
                       <th>Hash</th>
                   </tr>
               </thead>
               <tbody>
         """
         for block in self.chain:
            html_table += block.to_html_row()

         html_table += """
               </tbody>
           </table>
         </body>
         </html>
         """

         return html_table

def main():
    blockchain = Blockchain()

    blockchain.add_block("Transaction 1: Alice sent 10 coins to Bob")
    blockchain.add_block("Transaction 2: Bob sent 5 coins to Charlie")
    blockchain.add_block("Transaction 3: Charlie mined 2 coins")

    html_output = blockchain.generate_html_table()

    with open("blockchain_ledger.html", "w") as f:
         f.write(html_output)

    print("Blockchain ledger generated as blockchain_ledger.html")

if __name__ == "__main__":
    main()
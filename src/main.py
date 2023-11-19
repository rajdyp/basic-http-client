from http_client.client import HTTPClient
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch any homepage")
    parser.add_argument("server", help="Server or domain name")
    parser.add_argument("--port", type=int, default=80, help="Port number (default: 80)")
    parser.add_argument("--path", default="/", help="Path to the homepage (default: /)")

    args = parser.parse_args()

    # create an instance of HTTPClient
    http_client = HTTPClient(args.server, args.port)

    # fetch website
    http_client.get_website(args.path)

    # close connection
    http_client.close()

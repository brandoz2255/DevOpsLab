FROM grafana/grafana-enterprise

ENV GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource

EXPOSE 3000

CMD ["grafana-server", "--homepath=/usr/share/grafana"]

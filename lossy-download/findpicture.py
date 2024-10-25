import datetime

def tcp_packet(input_file):



def ipv4_packet(input_file):
    this_version = input_file[:1]
    this_ihl = input_file[1:2]
    this_length = input_file[4:8]
    this_length_int = int(this_length, 16)
    this_id = input_file[8:12]
    this_ttl = input_file[16:18]
    this_protocol = input_file[18:20]
    this_source_addr = input_file[24:32]
    this_dest_addr = input_file[32:40]
    print('this_version', this_version)
    print('this_ihl', this_ihl)
    print('this_length_int', this_length_int)
    print('this_protocol', this_protocol)
    print('this_source_addr', this_source_addr)
    print('this_dest_addr', this_dest_addr)
    input_file = input_file[40:]
    tcp_packet(input_file)




def ether_packet(input_file):
    j = 1
    
    hasPacket = True

    print('*** Ethernet packet ' + str(j) + ' ***')
    this_dest_addr = input_file[:12]
    this_source_addr = input_file[12:24]
    this_ether_type = input_file[24:28]
    print('this_dest_addr', this_dest_addr)
    print('this_source_addr', this_source_addr)
    print('this_ether_type', this_ether_type)
    input_file = input_file[28:]
    ipv4_packet(input_file)


    

def pcat_to_hex(input_file):
    with open(input_file, 'rb') as f:
        hex_file = f.read().hex()
        pcap_head = hex_file[:48]
        pcap_magic_n = pcap_head[:8]
        pcap_major_n = pcap_head[8:12]
        pcap_minor_n = pcap_head[12:16]
        pcap_reserved1 = pcap_head[16:24]
        pcap_reserved2 = pcap_head[24:32]
        pcap_snapshot_n = pcap_head[32:40]
        snapshot_length = int(pcap_snapshot_n, 16)
        pcap_link_layer = pcap_head[40:]
        print('pcap_head', pcap_head)
        print('pcap_magic_n', pcap_magic_n)
        print('pcap_major_n', pcap_major_n)
        print('pcap_minor_n', pcap_minor_n)
        print('pcap_reserved1', pcap_reserved1)
        print('pcap_reserved2', pcap_reserved2)
        print('pcap_snapshot_n', pcap_snapshot_n)
        print('snapshot_length', snapshot_length)
        print('pcap_link_layer', pcap_link_layer)
        new_input_file = hex_file[48:]
        print(len(new_input_file))
        packet_header = 32
        this_header = new_input_file[:32]
        this_time_stamp = this_header[:8]
        this_time_stamp_sec = int(this_time_stamp, 16)
        ts = datetime.datetime.fromtimestamp(this_time_stamp_sec).strftime('%Y-%m-%d %H:%M:%S')
        this_time_stamp_micro = this_header[8:16]
        this_time_stamp_micro_int = int(this_time_stamp_micro, 16)
        this_packet_length = this_header[16:24]
        this_packet_length_int = int(this_packet_length, 16)
        this_packet_untruncated_length = this_header[24:]
        print('this_header', this_header)
        print('this_time_stamp', this_time_stamp)
        print('this_time_stamp_sec', this_time_stamp_sec)
        print('ts', ts)
        print('this_time_stamp_micro',this_time_stamp_micro)
        print('this_time_stamp_micro_int', this_time_stamp_micro_int)
        print('this_packet_length', this_packet_length)
        print('this_packet_length_int', this_packet_length_int)
        print('this_packet_untruncated_length', this_packet_untruncated_length)
        print(this_packet_length == this_packet_untruncated_length)
        if(this_packet_untruncated_length):
            new_input_file = new_input_file[32:]
            ether_packet(new_input_file)
 









    
    with open('lossy_hex.txt', 'w') as hex_output:
        hex_output.write(hex_file)

input_file = 'lossy.pcap'
lossy_hex = pcat_to_hex(input_file)

# def capture_pcap_head(hexa):
#     header_len = 24
#     header_len_hex = header_len * 2
#     with open(hexa, 'rb') as h:
#         print(h)

# capture_pcap_head(lossy_hex)
# Copyright (c) 2024, Sahil Patel and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.file_manager import save_file
from frappe.model.document import Document


class PaymentCollection(Document):

	# def on_update(self):
	# 	email_ids = frappe.db.sql("select email_id from `tabEmail Recipients` where parent='Support Setup'",as_dict=1)
	# 	email_list = [item['email_id'] for item in email_ids]
	# 	payment_date = frappe.utils.formatdate(self.date, "dd-MM-yyyy")

	# 	message = f"""Dear {self.customer},<br><br>

	# 	We are pleased to inform you that your payment has been successfully completed.<br><br>

	# 	<strong>Transaction Details:</strong>
	# 	<ul>
	# 		<li><strong>Amount Paid:</strong> {self.grand_total}</li>
	# 		<li><strong>Date:</strong> {payment_date}</li>
	# 	</ul>"""

	# 	table_rows = ""
	# 	if self.payments:
	# 		# Fetch data for each payment ID
	# 		for payment_id in self.payments:
	# 			try:
	# 				print(payment_id)
				
	# 				item_code = payment_id.item_code or "-"
	# 				quantity = payment_id.quantity or 0  # Default to 0 if None
	# 				amount = payment_id.amount or 0  # Default to 0 if None
	# 				remarks = payment_id.remarks or ""
	# 				table_rows += f"""
	# 					<tr style="border: 1px solid #ddd;">
	# 						<td style="border: 1px solid #ddd; padding: 8px;">{item_code}</td>
	# 						<td style="border: 1px solid #ddd; padding: 8px;">{quantity}</td>
	# 						<td style="border: 1px solid #ddd; padding: 8px;">{amount}</td>
	# 						<td style="border: 1px solid #ddd; padding: 8px;">{remarks}</td>
	# 					</tr>
	# 				"""
	# 			except frappe.DoesNotExistError:
	# 				# Skip if the payment ID is not found
	# 				continue

	# 		# Add the table only if rows exist
	# 		if table_rows:
	# 			table_html = f"""
	# 							<br>
	# 							<div style="width: 100%; clear: both;">
	# 								<h3 style="font-family: Arial, sans-serif; color: #333;">Payments</h3>
	# 								<table style="border: 1px solid #ddd; border-collapse: collapse; width: 50%; font-family: Arial, sans-serif; font-size: 14px; text-align: left; float: left;">
	# 									<thead style="background-color: #f2f2f2; color: #333;">
	# 										<tr style="border: 1px solid #ddd;">
	# 											<th style="border: 1px solid #ddd; padding: 8px;">Item Code</th>
	# 											<th style="border: 1px solid #ddd; padding: 8px;">Qty</th>
	# 											<th style="border: 1px solid #ddd; padding: 8px;">Amount</th>
	# 											<th style="border: 1px solid #ddd; padding: 8px;">Remarks</th>
	# 										</tr>
	# 									</thead>
	# 									<tbody>
	# 										{table_rows}
	# 									</tbody>
	# 								</table>
	# 							</div>
	# 							<br>
	# 							<br>
	# 						"""
	# 			message += table_html

	# 		pending_table_rows = ""
	# 		if self.pending_payment_collection:
	# 			# Fetch data for each payment ID
	# 			for payment_id in self.pending_payment_collection:
	# 				try:
	# 					item = payment_id.item or ""
	# 					remarks = payment_id.remarks or ""
	# 					amount = payment_id.amount or 0  # Default to 0 if None
	# 					pending_table_rows += f"""
	# 						<tr style="border: 1px solid #ddd;">
	# 							<td style="border: 1px solid #ddd; padding: 8px;">{item}</td>
	# 							<td style="border: 1px solid #ddd; padding: 8px;">{amount}</td>
	# 							<td style="border: 1px solid #ddd; padding: 8px;">{remarks}</td>
	# 						</tr>
	# 					"""
	# 				except frappe.DoesNotExistError:
	# 					# Skip if the payment ID is not found
	# 					continue

	# 			# Add the table only if rows exist
	# 			if pending_table_rows:
	# 				pending_payment = f"""
	# 									<br>
	# 									<br>
	# 									<div style="width: 100%; clear: both;">
	# 										<h3 style="margin-top:30px; color: #333;">Pending Payments</h3>
	# 										<table style="border: 1px solid #ddd; border-collapse: collapse; width: 50%; font-family: Arial, sans-serif; font-size: 14px; text-align: left; float: left;">
	# 											<thead style="background-color: #f2f2f2; color: #333;">
	# 												<tr style="border: 1px solid #ddd;">
	# 												    <th style="border: 1px solid #ddd; padding: 8px;">Item Code</th>
	# 												    <th style="border: 1px solid #ddd; padding: 8px;">Amount</th>
	# 													<th style="border: 1px solid #ddd; padding: 8px;">Remarks</th>
														
	# 												</tr>
	# 											</thead>
	# 											<tbody>
	# 												{pending_table_rows}
	# 											</tbody>
	# 										</table>
	# 									</div>
	# 									<br>
	# 									"""
	# 				message += pending_payment

		



	# 	admin_message = f"""Dear Sir/Medam,<br><br>

	# 					This is to inform you that the payment has been successfully processed.<br><br>

	# 					<strong>Details:</strong>
	# 					<ul>
	# 						<li><strong>Transaction ID:</strong> {self.name}</li>
	# 						<li><strong>Payment Date:</strong> {payment_date}</li>
	# 						<li><strong>Amount:</strong> {self.grand_total}</li>
	# 						<li><strong>Paid By:</strong> {self.customer}</li>
	# 					</ul>


	# 					"""
		
	# 	if self.payments:
	# 		admin_message += table_html
					
	# 	if self.pending_payment_collection:
	# 		admin_message += pending_payment



	# 	try:
	# 		frappe.sendmail(
	# 			recipients= self.customer_email_id_id,  
	# 			subject=frappe._('Payment Confirmation'),
	# 			message=message
	# 		)


	# 		frappe.sendmail(
	# 			recipients=email_list,  
	# 			subject=frappe._('Payment Confirmation'),
	# 			message=admin_message
	# 		)
			
	# 		frappe.email.queue.flush()
			
	# 	except frappe.OutgoingEmailError as e:
	# 		frappe.log_error(message=str(e), title="Email Sending Failed")

	# 	if self.maintenance_visit:
	# 		frappe.db.set_value("Maintenance Visit",self.maintenance_visit,"custom_payment_done",1)


# ====================================================SEND MAIL
	# def on_update(self):
	# 	# Fetch email recipients from the 'Support Setup' table
	# 	email_ids = frappe.db.sql(
	# 		"SELECT email_id FROM `tabEmail Recipients` WHERE parent='Support Setup'", as_dict=1
	# 	)
	# 	email_list = [item["email_id"] for item in email_ids]

	# 	# Format the payment date
	# 	payment_date = frappe.utils.formatdate(self.date, "dd-MM-yyyy")

	# 	# **Customer Email Template**
	# 	customer_message = f"""
	# 		<div style="font-family: Arial, sans-serif; font-size: 16px; color: #333; line-height: 1.8; max-width: 700px; margin: auto; border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9;">
	# 			<div style="background-color: #007bff; color: white; padding: 15px; text-align: center; border-radius: 8px 8px 0 0;">
	# 				<h2 style="margin: 0;">Payment Confirmation</h2>
	# 			</div>
	# 			<p style="margin-top: 20px;">Dear {self.customer},</p>
	# 			<p>We are pleased to inform you that your payment has been successfully processed. Below are the details:</p>
	# 			<div style="background-color: #ffffff; border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin-bottom: 20px;">
	# 				<h3 style="color: #007bff; margin-top: 0; text-align: center;">Transaction Summary</h3>
	# 				<table style="border-collapse: collapse; width: 100%; margin: auto;">
	# 					<tbody>
	# 						<tr style="background-color: #f2f2f2;">
	# 							<td style="padding: 10px; border: 1px solid #ddd;"><strong>Transaction ID:</strong></td>
	# 							<td style="padding: 10px; border: 1px solid #ddd;">{self.name}</td>
	# 						</tr>
	# 						<tr>
	# 							<td style="padding: 10px; border: 1px solid #ddd;"><strong>Payment Date:</strong></td>
	# 							<td style="padding: 10px; border: 1px solid #ddd;">{payment_date}</td>
	# 						</tr>
	# 						<tr style="background-color: #f2f2f2;">
	# 							<td style="padding: 10px; border: 1px solid #ddd;"><strong>Total Amount:</strong></td>
	# 							<td style="padding: 10px; border: 1px solid #ddd;">{self.grand_total}</td>
	# 						</tr>
	# 					</tbody>
	# 				</table>
	# 			</div>
	# 	"""

	# 	# Payment table rows
	# 	payment_rows = ""
	# 	if self.payments:
	# 		for payment in self.payments:
	# 			payment_rows += f"""
	# 				<tr>
	# 					<td style="padding: 10px; border: 1px solid #ddd;">{payment.item_code or "-"}</td>
	# 					<td style="padding: 10px; border: 1px solid #ddd;">{payment.quantity or 0}</td>
	# 					<td style="padding: 10px; border: 1px solid #ddd;">{payment.amount or 0}</td>
	# 					<td style="padding: 10px; border: 1px solid #ddd;">{payment.remarks or ""}</td>
	# 				</tr>
	# 			"""

	# 		if payment_rows:
	# 			payment_table = f"""
	# 				<h3 style="margin-top: 20px; color: #007bff; text-align: center;">Payment Details</h3>
	# 				<table style="border-collapse: collapse; width: 100%; margin: auto; background-color: #ffffff; border: 1px solid #ddd; border-radius: 8px;">
	# 					<thead>
	# 						<tr style="background-color: #007bff; color: white;">
	# 							<th style="padding: 10px; border: 1px solid #ddd;">Item Code</th>
	# 							<th style="padding: 10px; border: 1px solid #ddd;">Quantity</th>
	# 							<th style="padding: 10px; border: 1px solid #ddd;">Amount</th>
	# 							<th style="padding: 10px; border: 1px solid #ddd;">Remarks</th>
	# 						</tr>
	# 					</thead>
	# 					<tbody>{payment_rows}</tbody>
	# 				</table>
	# 			"""
	# 			customer_message += payment_table

	# 	# Pending payments table
	# 	pending_rows = ""
	# 	if self.pending_payment_collection:
	# 		for pending in self.pending_payment_collection:
	# 			pending_rows += f"""
	# 				<tr>
	# 					<td style="padding: 10px; border: 1px solid #ddd;">{pending.amount or 0}</td>
	# 					<td style="padding: 10px; border: 1px solid #ddd;">{pending.remarks or ""}</td>
	# 				</tr>
	# 			"""

	# 		if pending_rows:
	# 			pending_table = f"""
	# 				<h3 style="margin-top: 20px; color: #e74c3c; text-align: center;">Pending Payments</h3>
	# 				<table style="border-collapse: collapse; width: 100%; margin: auto; background-color: #ffffff; border: 1px solid #ddd; border-radius: 8px;">
	# 					<thead>
	# 						<tr style="background-color: #e74c3c; color: white;">
	# 							<th style="padding: 10px; border: 1px solid #ddd;">Amount</th>
	# 							<th style="padding: 10px; border: 1px solid #ddd;">Remarks</th>
	# 						</tr>
	# 					</thead>
	# 					<tbody>{pending_rows}</tbody>
	# 				</table>
	# 			"""
	# 			customer_message += pending_table

	# 	# Closing message body
	# 	customer_message += """
	# 		<p style="margin-top: 20px;">Thank you for your business!</p>
	# 		<div style="text-align: center; padding: 10px; font-size: 14px; color: #777; border-top: 1px solid #ddd;">
	# 			<p style="margin: 0;">This is an automated email. Please do not reply.</p>
	# 		</div>
	# 	</div>
	# 	"""

	# 	# **Admin Email Template**
	# 	admin_message = f"""
	# 		<div style="font-family: Arial, sans-serif; font-size: 16px; color: #333; line-height: 1.8; max-width: 700px; margin: auto; border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9;">
	# 			<div style="background-color: #007bff; color: white; padding: 15px; text-align: center; border-radius: 8px 8px 0 0;">
	# 				<h2 style="margin: 0;">Payment Collection</h2>
	# 			</div>
	# 			<p style="margin-top: 20px;">Dear Sir/Medam,</p>
	# 			<p>This is to inform you that the payment has been successfully processed. Below are the details:</p>
	# 			<div style="background-color: #ffffff; border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin-bottom: 20px;">
	# 				<h3 style="color: #007bff; margin-top: 0; text-align: center;">Transaction Summary</h3>
	# 				<table style="border-collapse: collapse; width: 100%; margin: auto;">
	# 					<tbody>
	# 						<tr style="background-color: #f2f2f2;">
	# 							<td style="padding: 10px; border: 1px solid #ddd;"><strong>Transaction ID:</strong></td>
	# 							<td style="padding: 10px; border: 1px solid #ddd;">{self.name}</td>
	# 						</tr>
	# 						<tr>
	# 							<td style="padding: 10px; border: 1px solid #ddd;"><strong>Payment Date:</strong></td>
	# 							<td style="padding: 10px; border: 1px solid #ddd;">{payment_date}</td>
	# 						</tr>
	# 						<tr style="background-color: #f2f2f2;">
	# 							<td style="padding: 10px; border: 1px solid #ddd;"><strong>Total Amount:</strong></td>
	# 							<td style="padding: 10px; border: 1px solid #ddd;">{self.grand_total}</td>
	# 						</tr>
	# 						<tr>
	# 							<td style="padding: 10px; border: 1px solid #ddd;"><strong>Paid By:</strong></td>
	# 							<td style="padding: 10px; border: 1px solid #ddd;">{self.customer}</td>
	# 						</tr>
	# 					</tbody>
	# 				</table>
	# 			</div>
	# 			<h3 style="margin-top: 20px; color: #007bff; text-align: center;">Payment Details</h3>
	# 			<table style="border-collapse: collapse; width: 100%; margin: auto; background-color: #ffffff; border: 1px solid #ddd; border-radius: 8px;">
	# 				<thead>
	# 					<tr style="background-color: #007bff; color: white;">
	# 						<th style="padding: 10px; border: 1px solid #ddd;">Item Code</th>
	# 						<th style="padding: 10px; border: 1px solid #ddd;">Quantity</th>
	# 						<th style="padding: 10px; border: 1px solid #ddd;">Amount</th>
	# 						<th style="padding: 10px; border: 1px solid #ddd;">Remarks</th>
	# 					</tr>
	# 				</thead>
	# 				<tbody>{payment_rows}</tbody>
	# 			</table>
	# 			<h3 style="margin-top: 20px; color: #e74c3c; text-align: center;">Pending Payments</h3>
	# 			<table style="border-collapse: collapse; width: 100%; margin: auto; background-color: #ffffff; border: 1px solid #ddd; border-radius: 8px;">
	# 				<thead>
	# 					<tr style="background-color: #e74c3c; color: white;">
	# 						<th style="padding: 10px; border: 1px solid #ddd;">Amount</th>
	# 						<th style="padding: 10px; border: 1px solid #ddd;">Remarks</th>
	# 					</tr>
	# 				</thead>
	# 				<tbody>{pending_rows}</tbody>
	# 			</table>
	# 			<p style="margin-top: 20px;">Thank you.</p>
	# 			<div style="text-align: center; padding: 10px; font-size: 14px; color: #777; border-top: 1px solid #ddd;">
	# 				<p style="margin: 0;">This is an automated email for payment notifications.</p>
	# 			</div>
	# 		</div>
	# 	"""

	# 	# Send the emails to admin and customer
	# 	frappe.sendmail(
	# 		recipients=email_list,
	# 		subject="Payment Collection",
	# 		content=admin_message,

	# 	)

	# 	frappe.sendmail(
	# 		recipients=self.customer_email_id,
	# 		subject="Payment Confirmation",
	# 		content=customer_message,

	# 	)
	# 	frappe.email.queue.flush()





	def on_update(self):
			# Fetch email recipients from the 'Support Setup' table
		email_ids = frappe.db.sql(
			"SELECT email_id FROM `tabEmail Recipients` WHERE parent='Support Setup'", as_dict=1
		)
		email_list = [item["email_id"] for item in email_ids]

		# Format the payment date
		payment_date = frappe.utils.formatdate(self.date, "dd-MM-yyyy")

		# **Customer Email Template**
		customer_message = f"""
			<div style="font-family: Arial, sans-serif; font-size: 16px; color: #333; line-height: 1.8; max-width: 700px; margin: auto; border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9;">
				<div style="background-color: #007bff; color: white; padding: 15px; text-align: center; border-radius: 8px 8px 0 0;">
					<h2 style="margin: 0;">Payment Confirmation</h2>
				</div>
				<p style="margin-top: 20px;">Dear {self.customer},</p>
				<p>We are pleased to inform you that your payment has been successfully processed. Below are the details:</p>
				<div style="background-color: #ffffff; border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin-bottom: 20px;">
					<h3 style="color: #007bff; margin-top: 0; text-align: center;">Transaction Summary</h3>
					<table style="border-collapse: collapse; width: 100%; margin: auto;">
						<tbody>
							<tr style="background-color: #f2f2f2;">
								<td style="padding: 10px; border: 1px solid #ddd;"><strong>Transaction ID:</strong></td>
								<td style="padding: 10px; border: 1px solid #ddd;">{self.name}</td>
							</tr>
							<tr>
								<td style="padding: 10px; border: 1px solid #ddd;"><strong>Payment Date:</strong></td>
								<td style="padding: 10px; border: 1px solid #ddd;">{payment_date}</td>
							</tr>
							<tr style="background-color: #f2f2f2;">
								<td style="padding: 10px; border: 1px solid #ddd;"><strong>Total Amount:</strong></td>
								<td style="padding: 10px; border: 1px solid #ddd;">{self.grand_total}</td>
							</tr>
						</tbody>
					</table>
				</div>
		"""

		# Payment table rows
		payment_rows = ""
		if self.payments:
			for payment in self.payments:
				payment_rows += f"""
					<tr>
						<td style="padding: 10px; border: 1px solid #ddd;">{payment.item_code or "-"}</td>
						<td style="padding: 10px; border: 1px solid #ddd;">{payment.quantity or 0}</td>
						<td style="padding: 10px; border: 1px solid #ddd;">{payment.amount or 0}</td>
						<td style="padding: 10px; border: 1px solid #ddd;">{payment.remarks or ""}</td>
					</tr>
				"""

			if payment_rows:
				payment_table = f"""
					<h3 style="margin-top: 20px; color: #007bff; text-align: center;">Payment Details</h3>
					<table style="border-collapse: collapse; width: 100%; margin: auto; background-color: #ffffff; border: 1px solid #ddd; border-radius: 8px;">
						<thead>
							<tr style="background-color: #007bff; color: white;">
								<th style="padding: 10px; border: 1px solid #ddd;">Item Code</th>
								<th style="padding: 10px; border: 1px solid #ddd;">Quantity</th>
								<th style="padding: 10px; border: 1px solid #ddd;">Amount</th>
								<th style="padding: 10px; border: 1px solid #ddd;">Remarks</th>
							</tr>
						</thead>
						<tbody>{payment_rows}</tbody>
					</table>
				"""
				customer_message += payment_table

		# Pending payments table
		pending_rows = ""
		if self.pending_payment_collection:
			for pending in self.pending_payment_collection:
				pending_rows += f"""
					<tr>
						<td style="padding: 10px; border: 1px solid #ddd;">{pending.amount or 0}</td>
						<td style="padding: 10px; border: 1px solid #ddd;">{pending.remarks or ""}</td>
					</tr>
				"""

			if pending_rows:
				pending_table = f"""
					<h3 style="margin-top: 20px; color: #e74c3c; text-align: center;">Pending Payments</h3>
					<table style="border-collapse: collapse; width: 100%; margin: auto; background-color: #ffffff; border: 1px solid #ddd; border-radius: 8px;">
						<thead>
							<tr style="background-color: #e74c3c; color: white;">
								<th style="padding: 10px; border: 1px solid #ddd;">Amount</th>
								<th style="padding: 10px; border: 1px solid #ddd;">Remarks</th>
							</tr>
						</thead>
						<tbody>{pending_rows}</tbody>
					</table>
				"""
				customer_message += pending_table

		# Closing message body
		customer_message += """
			<p style="margin-top: 20px;">Thank you for your business!</p>
			<div style="text-align: center; padding: 10px; font-size: 14px; color: #777; border-top: 1px solid #ddd;">
				<p style="margin: 0;">This is an automated email. Please do not reply.</p>
			</div>
		</div>
		"""

		# **Admin Email Template**
		admin_message = f"""
			<div style="font-family: Arial, sans-serif; font-size: 16px; color: #333; line-height: 1.8; max-width: 700px; margin: auto; border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9;">
				<div style="background-color: #007bff; color: white; padding: 15px; text-align: center; border-radius: 8px 8px 0 0;">
					<h2 style="margin: 0;">Payment Collection</h2>
				</div>
				<p style="margin-top: 20px;">Dear Sir/Medam,</p>
				<p>This is to inform you that the payment has been successfully processed. Below are the details:</p>
				<div style="background-color: #ffffff; border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin-bottom: 20px;">
					<h3 style="color: #007bff; margin-top: 0; text-align: center;">Transaction Summary</h3>
					<table style="border-collapse: collapse; width: 100%; margin: auto;">
						<tbody>
							<tr style="background-color: #f2f2f2;">
								<td style="padding: 10px; border: 1px solid #ddd;"><strong>Transaction ID:</strong></td>
								<td style="padding: 10px; border: 1px solid #ddd;">{self.name}</td>
							</tr>
							<tr>
								<td style="padding: 10px; border: 1px solid #ddd;"><strong>Payment Date:</strong></td>
								<td style="padding: 10px; border: 1px solid #ddd;">{payment_date}</td>
							</tr>
							<tr style="background-color: #f2f2f2;">
								<td style="padding: 10px; border: 1px solid #ddd;"><strong>Total Amount:</strong></td>
								<td style="padding: 10px; border: 1px solid #ddd;">{self.grand_total}</td>
							</tr>
							<tr>
								<td style="padding: 10px; border: 1px solid #ddd;"><strong>Paid By:</strong></td>
								<td style="padding: 10px; border: 1px solid #ddd;">{self.customer}</td>
							</tr>
						</tbody>
					</table>
				</div>
				<h3 style="margin-top: 20px; color: #007bff; text-align: center;">Payment Details</h3>
				<table style="border-collapse: collapse; width: 100%; margin: auto; background-color: #ffffff; border: 1px solid #ddd; border-radius: 8px;">
					<thead>
						<tr style="background-color: #007bff; color: white;">
							<th style="padding: 10px; border: 1px solid #ddd;">Item Code</th>
							<th style="padding: 10px; border: 1px solid #ddd;">Quantity</th>
							<th style="padding: 10px; border: 1px solid #ddd;">Amount</th>
							<th style="padding: 10px; border: 1px solid #ddd;">Remarks</th>
						</tr>
					</thead>
					<tbody>{payment_rows}</tbody>
				</table>
				<h3 style="margin-top: 20px; color: #e74c3c; text-align: center;">Pending Payments</h3>
				<table style="border-collapse: collapse; width: 100%; margin: auto; background-color: #ffffff; border: 1px solid #ddd; border-radius: 8px;">
					<thead>
						<tr style="background-color: #e74c3c; color: white;">
							<th style="padding: 10px; border: 1px solid #ddd;">Amount</th>
							<th style="padding: 10px; border: 1px solid #ddd;">Remarks</th>
						</tr>
					</thead>
					<tbody>{pending_rows}</tbody>
				</table>
				<p style="margin-top: 20px;">Thank you.</p>
				<div style="text-align: center; padding: 10px; font-size: 14px; color: #777; border-top: 1px solid #ddd;">
					<p style="margin: 0;">This is an automated email for payment notifications.</p>
				</div>
			</div>
		"""

		# Use enqueue to send the emails in the background
		frappe.enqueue(
			send_payment_emails, 
			email_list=email_list, 
			customer_email_id=self.customer_email_id, 
			admin_message=admin_message, 
			customer_message=customer_message
		)






	def on_cancel(self):
		if self.maintenance_visit:
			frappe.db.set_value("Maintenance Visit",self.maintenance_visit,"custom_payment_done",0)




def send_payment_emails(email_list, customer_email_id, admin_message, customer_message):
    # Send the emails to admin and customer
    frappe.sendmail(
        recipients=email_list,
        subject="Payment Collection",
        content=admin_message,
    )

    frappe.sendmail(
        recipients=customer_email_id,
        subject="Payment Confirmation",
        content=customer_message,
    )

    # Ensure emails are sent in the background
    frappe.email.queue.flush()

@frappe.whitelist()
def get_unique_sold_items_by_customer(customer):
		# Fetch all submitted Sales Invoices for the given customer
		invoices = frappe.get_all('Sales Invoice', 
								filters={'customer': customer, 'docstatus': 1},  # docstatus=1 means submitted invoices
								fields=['name'])

		# Extract all item codes from these invoices
		sold_items = frappe.get_all('Sales Invoice Item', 
									filters={'parent': ['in', [invoice['name'] for invoice in invoices]]}, 
									fields=['item_code'])

		# Get unique item codes
		unique_items = list(set([item['item_code'] for item in sold_items]))

		return unique_items



@frappe.whitelist()
def get_customer_outstanding(customer):
    if not customer:
        frappe.throw("Customer is required.")

    outstanding = frappe.db.sql("""
        SELECT 
            SUM(outstanding_amount) AS outstanding_amount
        FROM 
            `tabSales Invoice`
        WHERE 
            docstatus = 1
            AND customer = %(customer)s
    """, {"customer": customer}, as_dict=True)

    return outstanding[0].outstanding_amount if outstanding and outstanding[0].outstanding_amount else 0



@frappe.whitelist()
def upload_image():
	uploaded_file = frappe.request.files['file']
	file_name = uploaded_file.filename
	file_content = uploaded_file.read()
	file_doc = save_file(file_name, file_content, None, None, is_private=False)
	return {
        "file_url": file_doc.file_url
    }
